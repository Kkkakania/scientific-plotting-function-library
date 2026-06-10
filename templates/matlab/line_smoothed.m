function fig = line_smoothed()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1); c = palette('cat', 1);
    x = linspace(0, 10, 300); y = sin(x) + 0.3*randn(1, 300);
    w = 10; y_s = filter(ones(1,w)/w, 1, y);
    fig = figure;
    plot(x, y, 'Color', [0.75 0.75 0.75], 'LineWidth', 0.8); hold on;
    plot(x, y_s, 'Color', c, 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Raw vs smoothed');
    legend({'raw','MA(10)'}); grid on;
end
