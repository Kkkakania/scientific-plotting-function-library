function fig = survival_km()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    scales = [18.0 10.0]; n = 60;
    names = {'Treatment', 'Control'};
    marks = 0:6:24;
    fig = figure('Position',[100 100 600 520]);
    ax = subplot(4, 1, 1:3); hold(ax, 'on');
    axt = subplot(4, 1, 4); hold(axt, 'on');
    hs = gobjects(1, 2);
    for g = 1:2
        true_t = -scales(g) * log(rand(n, 1));       % exponential lifetimes
        cens_t = 5 + 19 * rand(n, 1);                % uniform censoring 5..24
        t = min(true_t, cens_t);
        event = double(true_t <= cens_t);
        [t, order] = sort(t); event = event(order);
        at_risk = (n:-1:1)';
        s = cumprod(1 - event ./ at_risk);           % Kaplan-Meier by hand
        c = palette('cat',g);
        hs(g) = stairs(ax, [0; t], [1; s], 'Color', c, 'LineWidth', 1.5);
        cmask = event == 0;
        plot(ax, t(cmask), s(cmask), '+', 'Color', c, 'MarkerSize', 6, ...
             'LineWidth', 1.2, 'LineStyle', 'none');  % censoring marks
        for m = marks
            text(axt, m, 0.66 - 0.38*(g-1), sprintf('%d', sum(t >= m)), ...
                 'HorizontalAlignment', 'center', 'FontSize', 8, 'Color', c);
        end
        text(axt, -1.2, 0.66 - 0.38*(g-1), names{g}, 'HorizontalAlignment', ...
             'right', 'FontSize', 8, 'Color', c);
    end
    ylabel(ax, 'survival probability');
    ylim(ax, [0 1.04]); xlim(ax, [-4 25]);
    title(ax, 'Kaplan-Meier survival');
    legend(ax, hs, names, 'Location', 'northeast');
    grid(ax, 'on');
    set(ax, 'XTickLabel', []);
    ylim(axt, [0 1]); xlim(axt, [-4 25]);
    set(axt, 'YTick', []);
    xlabel(axt, 'time (months)');
    ylabel(axt, 'at risk', 'FontSize', 8);
end
