function fig = line_filled()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat', 1);
    x = linspace(0, 10, 200); y = exp(-x/4).*sin(2*x) + 1;
    fig = figure;
    fill([x, fliplr(x)], [y, zeros(size(y))], c, 'FaceAlpha', 0.3, 'EdgeColor','none'); hold on;
    plot(x, y, 'Color', c, 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Filled line'); grid on;
end
