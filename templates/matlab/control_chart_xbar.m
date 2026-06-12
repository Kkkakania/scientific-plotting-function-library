function fig = control_chart_xbar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    n_grp = 25; n_sub = 5;                     % 25 subgroups x 5 samples
    X = 10 + randn(n_grp, n_sub);
    X(20:end, :) = X(20:end, :) + 1.6;         % injected mean shift
    xbar = mean(X, 2)';
    R = (max(X, [], 2) - min(X, [], 2))';
    A2 = 0.577; D3 = 0.0; D4 = 2.114;          % control chart constants, n=5
    xbb = mean(xbar); rbar = mean(R);
    lims = {[xbb - A2*rbar, xbb + A2*rbar], [D3*rbar, D4*rbar]};
    vals = {xbar, R}; ctrs = [xbb, rbar];
    names = {'subgroup mean', 'subgroup range'};
    g = 1:n_grp;
    c0 = palette('cat', 1); c1 = palette('cat', 2);
    c2 = palette('cat', 3); c7 = palette('cat', 8);
    fig = figure('Position', [100 100 700 500]);
    for k = 1:2
        ax = subplot(2, 1, k); hold(ax, 'on');
        v = vals{k}; lim = lims{k};
        plot(g, v, '-o', 'Color', c0, 'MarkerSize', 4, 'MarkerFaceColor', c0);
        hc = yline(ctrs(k), '-', 'Color', c2, 'LineWidth', 1.2);
        yline(lim(1), '--', 'Color', c7, 'LineWidth', 1);
        yline(lim(2), '--', 'Color', c7, 'LineWidth', 1);
        out = v > lim(2) | v < lim(1);
        ho = plot(g(out), v(out), 'o', 'Color', c1, 'MarkerFaceColor', c1, ...
                  'MarkerSize', 6);
        ylabel(names{k}); grid on;
        if k == 1
            title('X-bar / R control chart');
            if any(out)
                legend([hc ho], {'center line', 'out of control'}, ...
                       'Location', 'northwest', 'FontSize', 7);
            else
                legend(hc, {'center line'}, 'Location', 'northwest', 'FontSize', 7);
            end
        end
    end
    xlabel('subgroup number');
end
