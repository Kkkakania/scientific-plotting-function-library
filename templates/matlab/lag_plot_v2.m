function fig = lag_plot_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(12);
    n = 400;
    y = zeros(1, n);
    for i = 2:n
        y(i) = 0.75*y(i-1) + randn;           % AR(1) demo series
    end
    fig = figure('Position', [100 100 600 550]);
    for k = 1:4
        subplot(2, 2, k); hold on;
        scatter(y(1:end-k), y(1+k:end), 8, palette('cat',1), 'filled', ...
                'MarkerFaceAlpha', 0.5);
        r = corrcoef(y(1:end-k), y(1+k:end));
        text(0.05, 0.92, sprintf('lag=%d, r=%.2f', k, r(1, 2)), ...
             'Units', 'normalized', 'FontSize', 8, 'Color', palette('cat',2));
        grid on;
        if k > 2, xlabel('y(t)'); end
        if mod(k, 2) == 1, ylabel('y(t+k)'); end
    end
    sgtitle('Lag plot matrix');
end
