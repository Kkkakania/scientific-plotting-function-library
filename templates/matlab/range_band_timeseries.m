function fig = range_band_timeseries()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(22);
    weeks = 1:52;
    season = 18 + 9 * sin((weeks - 12) * 2*pi / 52);
    hist = repmat(season, 9, 1) + 2.0 * randn(9, 52);   % 9 historical years
    hist = hist + 1.2 * randn(9, 1);                    % per-year offset
    now_w = 23;                                         % current year up to week 23
    this_year = season(1:now_w) + 2.5 + 1.0 * randn(1, now_w);
    lo = min(hist, [], 1); hi = max(hist, [], 1);
    c0 = palette('cat',1); c1 = palette('cat',2);
    fig = figure('Position',[100 100 700 400]); hold on;
    hband = fill([weeks fliplr(weeks)], [lo fliplr(hi)], c0, ...
                 'FaceAlpha', 0.18, 'EdgeColor', 'none');
    hmean = plot(weeks, mean(hist, 1), '--', 'Color', c0, 'LineWidth', 1.4);
    hcur = plot(weeks(1:now_w), this_year, 'Color', c1, 'LineWidth', 2);
    plot(now_w, this_year(end), 'o', 'Color', c1, 'MarkerFaceColor', c1, ...
         'MarkerSize', 5);
    text(now_w + 0.8, this_year(end) + 0.5, 'latest', 'FontSize', 8);
    xlabel('week of year'); ylabel('temperature (°C)');
    title('This year vs historical range');
    legend([hband hmean hcur], ...
           {'historical min-max', 'historical mean', 'current year'}, ...
           'Location', 'northwest', 'FontSize', 8, 'Box', 'off');
    grid on;
end
