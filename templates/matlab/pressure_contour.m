function fig = pressure_contour()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-2,4,200), linspace(-2,2,100));
    r2 = X.^2 + Y.^2 + 0.05;
    P = 1 - (1 - (X.^2 - Y.^2)./r2.^2).^2 - (2*X.*Y./r2.^2).^2;
    fig = figure('Position',[100 100 700 500]);
    contourf(X, Y, P, 25, 'LineStyle','none'); hold on;
    contour(X, Y, P, 12, 'k', 'LineWidth', 0.4);
    rectangle('Position',[-0.3 -0.3 0.6 0.6], 'Curvature',[1 1], 'FaceColor',[0.5 0.5 0.5]);
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'Cp';
    xlabel('x'); ylabel('y'); title('Pressure contour'); axis equal tight;
end
