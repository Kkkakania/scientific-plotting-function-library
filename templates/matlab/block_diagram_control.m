function fig = block_diagram_control()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position', [100 100 760 330]); hold on;
    axis([0 12 0 5]); axis off; daspect([1 1 1]);
    lc = [0.25 0.25 0.25];
    % 求和点
    sx = 2.6; sy = 3.2;
    tt = linspace(0, 2*pi, 50);
    fill(sx + 0.22*cos(tt), sy + 0.22*sin(tt), 'w', 'EdgeColor', lc, 'LineWidth', 1.2);
    text(sx - 0.34, sy + 0.30, '+', 'FontSize', 10);
    text(sx - 0.10, sy - 0.48, '-', 'FontSize', 12);
    bbox(4.8, 3.2, 1.9, 1.0, sprintf('PID\ncontroller'), [0.86 0.91 0.96], [0.18 0.31 0.47]);
    bbox(7.6, 3.2, 1.9, 1.0, sprintf('Plant\nG(s)'),      [0.86 0.91 0.96], [0.18 0.31 0.47]);
    bbox(5.7, 1.3, 1.9, 0.9, sprintf('Sensor\nH(s)'),     [0.96 0.86 0.86], [0.54 0.19 0.20]);
    harrow(0.8, 3.2, sx - 0.22, 3.2);  text(0.75, 3.5, 'r(t)', 'FontSize', 9);
    harrow(sx + 0.22, 3.2, 3.85, 3.2); text(3.1, 3.5, 'e(t)', 'FontSize', 9);
    harrow(5.75, 3.2, 6.65, 3.2);      text(6.0, 3.5, 'u(t)', 'FontSize', 9);
    harrow(8.55, 3.2, 11.2, 3.2);      text(10.6, 3.5, 'y(t)', 'FontSize', 9);
    plot(10.2, 3.2, '.', 'Color', lc, 'MarkerSize', 12);
    plot([10.2 10.2 6.65], [3.2 1.3 1.3], 'Color', lc, 'LineWidth', 1.1);
    plot([4.75 sx sx], [1.3 1.3 NaN], 'Color', lc, 'LineWidth', 1.1);
    plot([4.75 sx], [1.3 1.3], 'Color', lc, 'LineWidth', 1.1);
    q = quiver(sx, 1.3, 0, sy - 0.22 - 1.3, 0, 'Color', lc, 'LineWidth', 1.1, 'MaxHeadSize', 0.4);
    q.AutoScale = 'off';
    title('Closed-loop control block diagram');
end

function bbox(cx, cy, w, h, txt, fc, ec)
    rectangle('Position', [cx-w/2 cy-h/2 w h], 'Curvature', 0.12, ...
              'FaceColor', fc, 'EdgeColor', ec, 'LineWidth', 1.2);
    text(cx, cy, txt, 'HorizontalAlignment', 'center', 'FontSize', 8.5);
end

function harrow(x1, y1, x2, y2)
    q = quiver(x1, y1, x2-x1, y2-y1, 0, 'Color', [0.25 0.25 0.25], ...
           'LineWidth', 1.1, 'MaxHeadSize', 0.25/max(abs(x2-x1), 0.3));
    q.AutoScale = 'off';
end
