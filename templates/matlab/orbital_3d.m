function fig = orbital_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    theta = linspace(0, pi, 80); phi = linspace(0, 2*pi, 80);
    [THETA, PHI] = meshgrid(theta, phi);
    % 简化球谐近似：Y_3,2 形状
    Y = sin(THETA).^2 .* cos(THETA) .* cos(2*PHI);
    R = abs(Y);
    X = R.*sin(THETA).*cos(PHI);
    Yp = R.*sin(THETA).*sin(PHI);
    Z = R.*cos(THETA);
    fig = figure('Position',[100 100 650 500]);
    surf(X, Yp, Z, Y, 'EdgeColor','none');
    colormap(palette('div')); shading interp;
    xlabel('x'); ylabel('y'); zlabel('z'); title('Spherical harmonic (Y_{3,2})');
    view(45, 30); axis equal;
end
