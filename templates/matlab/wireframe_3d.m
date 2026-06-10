function fig = wireframe_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3, 3, 40));
    Z = peaks(X, Y);
    fig = figure('Position',[100 100 650 500]);
    mesh(X, Y, Z, 'EdgeColor', palette('cat',1)); hold on;
    contour3(X, Y, Z, 15, 'k', 'LineWidth', 0.5);
    xlabel('x'); ylabel('y'); zlabel('z'); title('Wireframe + projection');
    view(45, 25);
end
