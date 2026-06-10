function fig = cross_correlation()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(24); c = palette('cat',1);
    n = 500; x = randn(1, n); y = circshift(x, 15) + 0.4*randn(1, n);
    x = x - mean(x); y = y - mean(y);
    [xc, lags] = xcorr(y, x, 'coeff');
    fig = figure;
    mask = lags >= -50 & lags <= 50;
    stem(lags(mask), xc(mask), 'Color', c, 'LineWidth', 1, 'MarkerFaceColor', c);
    xline(0, 'k');
    xlabel('lag'); ylabel('xcorr'); title('Cross-correlation'); grid on;
end
