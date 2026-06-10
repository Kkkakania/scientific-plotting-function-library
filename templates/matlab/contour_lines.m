function fig = contour_lines()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3, 3, 80));
    Z = peaks(X, Y);
    fig = figure;
    [C, h] = contour(X, Y, Z, 12, 'LineWidth', 1);
    colormap(parula);
    clabel(C, h, 'FontSize', 7);
    xlabel('x'); ylabel('y'); title('Contour lines');
end
