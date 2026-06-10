function fig = isosurface_plot(level)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    if nargin<1, level = 1.5; end
    apply_theme();
    n = 40;
    [X, Y, Z] = meshgrid(linspace(-2, 2, n));
    V = X.^2 + Y.^2 + Z.^2;
    fig = figure('Position',[100 100 650 500]);
    p = patch(isosurface(X, Y, Z, V, level));
    p.FaceColor = palette('cat',1); p.EdgeColor = 'none';
    daspect([1 1 1]); camlight; lighting gouraud;
    xlabel('x'); ylabel('y'); zlabel('z');
    title(sprintf('Isosurface V=%g', level));
    view(45, 30); grid on;
end
