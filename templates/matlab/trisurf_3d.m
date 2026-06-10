function fig = trisurf_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(23);
    n = 200;
    x = 4*rand(n,1) - 2; y = 4*rand(n,1) - 2;
    z = exp(-(x.^2 + y.^2)/2);
    tri = delaunay(x, y);
    fig = figure('Position',[100 100 650 500]);
    trisurf(tri, x, y, z, 'EdgeColor','none');
    colormap(parula); cb = colorbar; cb.Label.String = 'z';
    xlabel('x'); ylabel('y'); zlabel('z'); title('Triangulated surface');
    view(45, 30);
end
