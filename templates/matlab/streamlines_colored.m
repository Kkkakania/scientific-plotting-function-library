function fig = streamlines_colored()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3,3,300), linspace(-2,2,200));
    U = 1 + 0.6*cos(X) - 0.3*Y;
    V = -0.4*Y + 0.3*sin(X);
    [sx, sy] = meshgrid(linspace(-3,3,12), linspace(-2,2,8));
    fig = figure('Position',[100 100 700 500]);
    hl = streamline(X, Y, U, V, sx, sy);
    set(hl, 'Color', palette('cat',1), 'LineWidth', 1);
    axis equal tight; xlabel('x'); ylabel('y'); title('Colored streamlines');
end
