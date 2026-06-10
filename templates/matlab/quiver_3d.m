function fig = quiver_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [x, y, z] = meshgrid(linspace(-2, 2, 6), linspace(-2, 2, 6), linspace(-2, 2, 6));
    u = -y; v = x; w = 0.3*z;
    fig = figure('Position',[100 100 650 500]);
    quiver3(x, y, z, u, v, w, 1.5, 'Color', palette('cat',1));
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D quiver field');
    view(45, 30); grid on;
end
