function fig = lyapunov_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-2, 2, 50));
    V = X.^2 + 0.5*X.*Y + Y.^2;
    fig = figure('Position',[100 100 650 500]);
    surf(X, Y, V, 'EdgeColor','none', 'FaceAlpha', 0.85); hold on;
    contour3(X, Y, V, 15);
    colormap(parula); colorbar;
    xlabel('x_1'); ylabel('x_2'); zlabel('V'); title('Lyapunov surface');
    view(45, 30);
end
