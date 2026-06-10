function fig = surface_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-8, 8, 60));
    R = sqrt(X.^2 + Y.^2) + eps; Z = sin(R)./R;
    fig = figure('Position',[100 100 650 500]);
    surf(X, Y, Z, 'EdgeColor','none');
    colormap(parula); cb = colorbar; cb.Label.String = 'z';
    shading interp; camlight; lighting gouraud;
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D surface');
    view(45, 30);
end
