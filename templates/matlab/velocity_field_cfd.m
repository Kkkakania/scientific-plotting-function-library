function fig = velocity_field_cfd()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-2,2,60), linspace(-1,1,40));
    U = 1 - X.^2 + 0.3*Y; V = -0.15*Y.*X;
    speed = hypot(U, V);
    fig = figure('Position',[100 100 700 500]);
    pcolor(X, Y, speed); shading interp; hold on;
    colormap(parula); colorbar;
    skip = 4;
    quiver(X(1:skip:end,1:skip:end), Y(1:skip:end,1:skip:end), ...
           U(1:skip:end,1:skip:end), V(1:skip:end,1:skip:end), 1.5, 'Color','w');
    xlabel('x'); ylabel('y'); title('Velocity field'); axis equal tight;
end
