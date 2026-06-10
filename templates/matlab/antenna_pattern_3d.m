function fig = antenna_pattern_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    phi   = linspace(0, 2*pi, 100);
    theta = linspace(0, pi, 60);
    [PHI, THETA] = meshgrid(phi, theta);
    R = abs(cos(THETA)).^2 .* abs(sin(2*PHI));
    X = R.*sin(THETA).*cos(PHI);
    Y = R.*sin(THETA).*sin(PHI);
    Z = R.*cos(THETA);
    fig = figure('Position',[100 100 650 500]);
    surf(X, Y, Z, R, 'EdgeColor','none');
    colormap(hot);
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D antenna pattern');
end
