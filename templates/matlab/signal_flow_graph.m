function fig = signal_flow_graph()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position', [100 140 760 300]); hold on;
    axis([0 12 0 5]); axis off; daspect([1 1 1]);
    names = {'R', 'E', 'X_1', 'X_2', 'Y'};
    xs = [1 3.2 5.4 7.6 9.8]; ys = 2.5*ones(1, 5);
    edge(1, 2, '1', 0, [0.25 0.25 0.25], xs, ys);
    edge(2, 3, 'G_1', 0, [0.25 0.25 0.25], xs, ys);
    edge(3, 4, 'G_2', 0, [0.25 0.25 0.25], xs, ys);
    edge(4, 5, 'G_3', 0, [0.25 0.25 0.25], xs, ys);
    edge(4, 3, '-H_1', 0.55, [0.66 0.45 0.10], xs, ys);
    edge(5, 2, '-H_2', 0.85, [0.77 0.31 0.32], xs, ys);
    for i = 1:5
        plot(xs(i), ys(i), 'o', 'MarkerSize', 9, 'MarkerFaceColor', [0.18 0.31 0.47], ...
             'MarkerEdgeColor', 'none');
        text(xs(i), ys(i) - 0.55, names{i}, 'HorizontalAlignment', 'center', 'FontSize', 9);
    end
    title('Signal-flow graph');
end

function edge(a, b, gain, bend, col, xs, ys)
    x1 = xs(a); y1 = ys(a); x2 = xs(b); y2 = ys(b);
    t = linspace(0, 1, 60);
    mx = (x1 + x2)/2; my = (y1 + y2)/2 + bend*2;
    bx = (1-t).^2*x1 + 2*(1-t).*t*mx + t.^2*x2;     % 二次贝塞尔
    by = (1-t).^2*y1 + 2*(1-t).*t*my + t.^2*y2;
    plot(bx(1:55), by(1:55), 'Color', col, 'LineWidth', 1.3);
    q = quiver(bx(55), by(55), bx(58)-bx(55), by(58)-by(55), 0, 'Color', col, ...
           'LineWidth', 1.3, 'MaxHeadSize', 6);
    q.AutoScale = 'off';
    text(mx, my + 0.28*sign(bend + 0.01), gain, 'HorizontalAlignment', 'center', ...
         'FontSize', 9, 'Color', col);
end
