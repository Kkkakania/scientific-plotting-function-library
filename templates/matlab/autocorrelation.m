function fig = autocorrelation()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1); c = palette('cat',1);
    n = 500; y = zeros(1, n);
    for i = 2:n, y(i) = 0.7*y(i-1) + randn; end
    y = y - mean(y);
    max_lag = 40;
    acf = zeros(1, max_lag+1);
    for k = 0:max_lag
        acf(k+1) = sum(y(1:n-k) .* y(k+1:n)) / sum(y.^2);
    end
    ci = 1.96 / sqrt(n);
    fig = figure;
    stem(0:max_lag, acf, 'Color', c, 'LineWidth', 1, 'MarkerFaceColor', c); hold on;
    yline( ci, '--', 'Color', [0.5 0.5 0.5]);
    yline(-ci, '--', 'Color', [0.5 0.5 0.5]);
    xlabel('lag'); ylabel('ACF'); title('Autocorrelation'); grid on;
end
