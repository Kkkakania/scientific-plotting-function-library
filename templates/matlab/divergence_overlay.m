function fig = divergence_overlay()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3,3,200));
    U = X + Y; V = X - Y;
    [Ux, ~] = gradient(U); [~, Vy] = gradient(V);
    div = Ux + Vy;
    fig = figure('Position',[100 100 600 500]);
    pcolor(X, Y, div); shading interp; hold on;
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'divergence';
    [sx, sy] = meshgrid(linspace(-3,3,10));
    hl = streamline(X, Y, U, V, sx, sy); set(hl, 'Color', 'k', 'LineWidth', 0.5);
    axis equal tight; xlabel('x'); ylabel('y'); title('Divergence + streamlines');
end
