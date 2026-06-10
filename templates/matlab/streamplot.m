function fig = streamplot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3,3,200));
    U = -1 - X.^2 + Y; V = 1 + X - Y.^2;
    [sx, sy] = meshgrid(linspace(-3,3,12));
    fig = figure;
    hl = streamline(X, Y, U, V, sx, sy);
    set(hl, 'Color', palette('cat',1));
    axis equal tight; xlabel('x'); ylabel('y'); title('Streamlines');
end
