function fig = line_log()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = logspace(-1, 3, 200);
    fig = figure;
    loglog(x, x.^2,   'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    loglog(x, x.^1.5, 'Color', palette('cat',2), 'LineWidth', 1.5);
    loglog(x, x.^0.5, 'Color', palette('cat',3), 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Log-scale line');
    legend({'x^2','x^{1.5}','\surd x'}); grid on;
end
