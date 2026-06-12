function fig = seasonal_subseries_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(21);
    months = {'Jan','Feb','Mar','Apr','May','Jun', ...
              'Jul','Aug','Sep','Oct','Nov','Dec'};
    n_years = 6;
    season = 10 + 4 * sin(((0:11) - 2) * pi / 6);
    M = repmat(season, n_years, 1) + 0.5 * (0:n_years-1)' ...
        + 0.6 * randn(n_years, 12);                  % years x months
    yl = [min(M(:)) - 0.6, max(M(:)) + 0.6];
    fig = figure('Position',[100 100 900 320]);
    for m = 1:12
        subplot(1, 12, m); hold on;
        plot(0:n_years-1, M(:, m), '-o', 'Color', palette('cat',1), ...
             'MarkerFaceColor', palette('cat',1), 'MarkerSize', 2.5, ...
             'LineWidth', 1);
        mu = mean(M(:, m));
        plot([-0.4 n_years-0.6], [mu mu], 'Color', palette('cat',2), ...
             'LineWidth', 1.4);
        ylim(yl); xlim([-0.5 n_years-0.5]);
        set(gca, 'XTick', []);
        if m > 1, set(gca, 'YTickLabel', []); else, ylabel('value'); end
        xlabel(months{m}, 'FontSize', 7);
        set(gca, 'XGrid', 'off', 'YGrid', 'on');
    end
    sgtitle('Seasonal subseries (faceted by month)');
    annotation('textbox', [0 0 1 0.05], 'String', ...
               'year index within each month panel', 'FontSize', 8, ...
               'HorizontalAlignment', 'center', 'EdgeColor', 'none');
end
