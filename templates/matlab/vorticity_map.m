function fig = vorticity_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-2,2,200));
    U = -Y .* exp(-(X.^2 + Y.^2)/2);
    V =  X .* exp(-(X.^2 + Y.^2)/2);
    [dV_dx, ~] = gradient(V); [~, dU_dy] = gradient(U);
    omega = dV_dx - dU_dy;
    fig = figure('Position',[100 100 700 500]);
    pcolor(X, Y, omega); shading interp;
    colormap(palette('div')); cb = colorbar; cb.Label.String = '\omega';
    xlabel('x'); ylabel('y'); title('Vorticity field'); axis equal tight;
end
