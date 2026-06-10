function fig = scatter_regression()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5); c = palette('cat',1);
    x = 10*rand(60,1); y = 1.5*x + 2 + 2*randn(60,1);
    p = polyfit(x, y, 1);
    xs = linspace(min(x), max(x), 100); ys = polyval(p, xs);
    residual = y - polyval(p, x);
    se = std(residual);
    ci = 1.96 * se;
    fig = figure;
    fill([xs, fliplr(xs)], [ys-ci, fliplr(ys+ci)], c, 'FaceAlpha', 0.2, 'EdgeColor','none'); hold on;
    scatter(x, y, 30, c, 'filled', 'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w');
    plot(xs, ys, 'Color', c, 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Scatter with regression');
    legend({'95% CI','data', sprintf('y = %.2fx + %.2f', p(1), p(2))});
    grid on;
end
