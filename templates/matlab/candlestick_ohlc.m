function fig = candlestick_ohlc()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    n = 60;
    drift = 0.05 + 1.2*randn(1, n);
    closep = 100 + cumsum(drift);
    openp = [100, closep(1:end-1)] + 0.3*randn(1, n);
    highp = max(openp, closep) + (0.2 + 1.6*rand(1, n));
    lowp  = min(openp, closep) - (0.2 + 1.6*rand(1, n));
    vol = (0.4 + 0.6*rand(1, n)).*(1 + abs(drift));
    x = 1:n;
    up = closep >= openp;
    cu = palette('cat', 3); cd = palette('cat', 2);   % up green, down red-orange
    fig = figure('Position', [100 100 800 450]);
    tl = tiledlayout(4, 1, 'TileSpacing', 'compact');
    ax = nexttile(tl, [3 1]); hold(ax, 'on');
    plot(ax, [x; x], [lowp; highp], '-', 'Color', [0.4 0.4 0.4], 'LineWidth', 0.7);
    for i = 1:n
        if up(i), c = cu; else, c = cd; end
        rectangle(ax, 'Position', [i-0.3, min(openp(i), closep(i)), 0.6, ...
                  max(abs(closep(i)-openp(i)), 1e-6)], 'FaceColor', c, 'EdgeColor', 'none');
    end
    xlim(ax, [0 n+1]); ylabel(ax, 'price'); title(ax, 'OHLC candlestick');
    ax.YGrid = 'on'; set(ax, 'XTickLabel', []);
    axv = nexttile(tl); hold(axv, 'on');
    vol_up = vol; vol_up(~up) = nan;
    vol_dn = vol; vol_dn(up) = nan;
    bar(axv, x, vol_up, 0.6, 'FaceColor', cu, 'FaceAlpha', 0.6, 'EdgeColor', 'none');
    bar(axv, x, vol_dn, 0.6, 'FaceColor', cd, 'FaceAlpha', 0.6, 'EdgeColor', 'none');
    xlim(axv, [0 n+1]);
    xlabel(axv, 'trading day'); ylabel(axv, 'volume');
    axv.YGrid = 'on';
end
