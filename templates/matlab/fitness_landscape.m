function fig = fitness_landscape()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    [X, Y] = meshgrid(linspace(-3,3,200));
    Z = -(sin(sqrt(X.^2 + Y.^2)).^2 + 0.5*(X.^2 + Y.^2));
    pop = -2.5 + 5*rand(40, 2);
    fig = figure('Position',[100 100 700 500]);
    contourf(X, Y, Z, 20, 'LineStyle','none'); hold on;
    contour(X, Y, Z, 10, 'k', 'LineWidth', 0.4);
    scatter(pop(:,1), pop(:,2), 30, 'r', 'filled', 'MarkerEdgeColor','w');
    colormap(parula); cb = colorbar; cb.Label.String = 'fitness';
    xlabel('x_1'); ylabel('x_2'); title('Fitness landscape'); axis equal;
end
