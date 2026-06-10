function fig = scatter_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 300; x = randn(n,1); y = randn(n,1); z = randn(n,1);
    c = x.^2 + y.^2 + z.^2;
    fig = figure('Position',[100 100 650 500]);
    scatter3(x, y, z, 30, c, 'filled', 'MarkerEdgeColor','w');
    colormap(parula); cb = colorbar; cb.Label.String = 'value';
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D scatter');
    view(45, 25); grid on;
end
