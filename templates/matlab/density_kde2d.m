function fig = density_kde2d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    x = randn(1500, 1); y = 0.5*x + 0.7*randn(1500, 1);
    [xq, yq] = meshgrid(linspace(min(x), max(x), 80), linspace(min(y), max(y), 80));
    f = ksdensity([x y], [xq(:) yq(:)]);
    Z = reshape(f, size(xq));
    fig = figure;
    contourf(xq, yq, Z, 12, 'LineStyle','none'); hold on;
    scatter(x, y, 4, 'k', 'filled', 'MarkerFaceAlpha', 0.2);
    colormap(palette('seq_purple')); cb = colorbar; cb.Label.String = 'density';
    xlabel('x'); ylabel('y'); title('2D KDE contour');
end
