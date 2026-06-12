function fig = horizon_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    n_bands = 2;
    n = 400; n_series = 4;
    x = 0:n-1;
    Y = cumsum(randn(n_series, n), 2);
    Y = Y - mean(Y, 2);
    fig = figure('Position', [100 100 800 360]);
    for s = 1:n_series
        subplot(n_series, 1, s); hold on;
        y = Y(s, :);
        hb = max(abs(y)) / n_bands;           % band height
        for k = 0:n_bands-1
            pos = min(max(max(y, 0) - k*hb, 0), hb);
            neg = min(max(max(-y, 0) - k*hb, 0), hb);
            a = 0.35 + 0.5*k/max(n_bands - 1, 1);
            fill([x fliplr(x)], [pos zeros(1, n)], palette('cat',1), ...
                 'FaceAlpha', a, 'EdgeColor', 'none');
            fill([x fliplr(x)], [neg zeros(1, n)], palette('cat',2), ...
                 'FaceAlpha', a, 'EdgeColor', 'none');
        end
        xlim([0 n-1]); ylim([0 hb]);
        set(gca, 'YTick', []);
        ylabel(sprintf('S%d', s), 'Rotation', 0, 'HorizontalAlignment', 'right');
        if s == 1, title('Horizon chart'); end
        if s < n_series, set(gca, 'XTickLabel', []); end
    end
    xlabel('time (sample)');
end
