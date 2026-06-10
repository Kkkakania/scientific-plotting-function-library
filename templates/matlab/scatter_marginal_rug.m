function fig = scatter_marginal_rug()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0); c = palette('cat',1);
    x = randn(120,1); y = 0.7*x + 0.6*randn(120,1);
    fig = figure;
    scatter(x, y, 25, c, 'filled', 'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w'); hold on;
    yl = ylim; xl = xlim;
    for i = 1:numel(x)
        plot([x(i) x(i)], [yl(1) yl(1)+0.03*diff(yl)], 'Color', c, 'LineWidth', 0.6);
        plot([xl(1) xl(1)+0.012*diff(xl)], [y(i) y(i)], 'Color', c, 'LineWidth', 0.6);
    end
    xlabel('x'); ylabel('y'); title('Scatter with rug'); grid on;
end
