function fig = lag_plot(lag)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(18); if nargin < 1, lag = 1; end
    n = 500; y = zeros(1, n);
    for i = 2:n, y(i) = 0.8*y(i-1) + randn; end
    fig = figure;
    scatter(y(1:end-lag), y(lag+1:end), 15, palette('cat',1), 'filled', 'MarkerFaceAlpha', 0.6);
    xlabel('y(t)'); ylabel(sprintf('y(t+%d)', lag));
    title(sprintf('Lag plot (lag = %d)', lag)); grid on;
end
