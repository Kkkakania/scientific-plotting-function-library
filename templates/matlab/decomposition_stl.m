function fig = decomposition_stl()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(9);
    n_years = 8; period = 12; n = n_years*period;
    t = 0:n-1;
    y = 20 + 0.08*t + 2*sin(2*pi*t/96) + 4*sin(2*pi*t/period) ...
        + 1.5*cos(4*pi*t/period) + 0.8*randn(1, n);
    % 2x12 centered moving average for the trend
    w = ones(1, period)/period;
    ma = conv(y, w, 'valid');
    trend = nan(1, n);
    trend(period/2+1 : period/2+numel(ma)-1) = (ma(1:end-1) + ma(2:end))/2;
    detr = y - trend;
    seas_m = zeros(1, period);
    for m = 1:period
        seas_m(m) = mean(detr(m:period:end), 'omitnan');
    end
    seas_m = seas_m - mean(seas_m);
    seasonal = repmat(seas_m, 1, n_years);
    resid = y - trend - seasonal;
    parts = {y, trend, seasonal, resid};
    names = {'observed', 'trend', 'seasonal', 'residual'};
    fig = figure('Position', [100 100 700 650]);
    for i = 1:4
        ax = subplot(4, 1, i); hold(ax, 'on');
        if i == 4
            plot(t, parts{i}, '.', 'Color', palette('cat', 4), 'MarkerSize', 7);
            yline(0, '-', 'Color', [0.4 0.4 0.4], 'LineWidth', 0.8);
        else
            plot(t, parts{i}, 'Color', palette('cat', i), 'LineWidth', 1.2);
        end
        ylabel(names{i}); grid on; xlim([0 n-1]);
        if i == 1, title('Time-series decomposition'); end
        if i < 4, set(ax, 'XTickLabel', []); end
    end
    xlabel('time (month index)');
end
