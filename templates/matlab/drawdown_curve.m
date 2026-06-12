function fig = drawdown_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    n = 750;
    r = 0.0006 + 0.011*randn(1, n);
    equity = cumprod(1 + r);
    peak = cummax(equity);
    dd = equity./peak - 1;
    t = 0:n-1;
    [dd_min, i_mdd] = min(dd);
    c0 = palette('cat', 1); c1 = palette('cat', 2); c7 = palette('cat', 8);
    fig = figure('Position', [100 100 700 500]);
    tl = tiledlayout(3, 1, 'TileSpacing', 'compact');
    ax = nexttile(tl, [2 1]); hold(ax, 'on');
    plot(ax, t, equity, 'Color', c0, 'LineWidth', 1.5);
    plot(ax, t, peak, '--', 'Color', c7, 'LineWidth', 1);
    ylabel(ax, 'net asset value'); title(ax, 'Equity curve and drawdown');
    legend(ax, {'equity (NAV)', 'running peak'}, 'Location', 'northwest');
    grid(ax, 'on'); set(ax, 'XTickLabel', []); xlim(ax, [0 n-1]);
    axd = nexttile(tl); hold(axd, 'on');
    fill(axd, [t, fliplr(t)], [dd*100, zeros(1, n)], c1, ...
         'FaceAlpha', 0.5, 'EdgeColor', 'none');
    plot(axd, t, dd*100, 'Color', c1, 'LineWidth', 0.8);
    plot(axd, t(i_mdd), dd_min*100, 'v', 'Color', c1, ...
         'MarkerFaceColor', c1, 'MarkerSize', 6);
    text(axd, t(i_mdd)+12, dd_min*100, sprintf('max DD %.1f%%', dd_min*100), ...
         'FontSize', 8);
    xlabel(axd, 'trading day'); ylabel(axd, 'drawdown (%)');
    grid(axd, 'on'); xlim(axd, [0 n-1]);
end
