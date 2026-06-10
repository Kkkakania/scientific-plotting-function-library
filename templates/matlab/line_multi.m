function fig = line_multi()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 10, 100);
    fig = figure; hold on;
    for i = 1:4
        plot(x, sin(x + (i-1)*pi/4), 'Color', palette('cat', i), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('y'); title('Multi-line');
    legend(arrayfun(@(i)sprintf('series %d',i), 1:4, 'UniformOutput', false));
    grid on;
end
