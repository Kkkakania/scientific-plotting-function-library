function fig = contour_filled_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-8, 8, 60));
    R = sqrt(X.^2 + Y.^2) + eps; Z = sin(R)./R;
    fig = figure('Position',[100 100 650 500]);
    surf(X, Y, Z, 'EdgeColor','none', 'FaceAlpha', 0.6); hold on;
    contour3(X, Y, Z, 15, 'LineWidth', 1);
    colormap(parula);
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D filled contour');
    view(45, 30);
end
