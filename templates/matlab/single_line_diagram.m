function fig = single_line_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position', [100 80 720 540]); hold on;
    axis([0 12 0 9]); axis off; daspect([1 1 1]);
    lc = [0.19 0.19 0.19];
    for i = 1:2
        x = 3.5 + (i-1)*5;
        q = quiver(x, 8.7, 0, -1.1, 0, 'Color', lc, 'LineWidth', 1.4, 'MaxHeadSize', 0.4);
        q.AutoScale = 'off';
        text(x + 0.2, 8.45, sprintf('110 kV source %d', i), 'FontSize', 8);
        breaker(x, 7.3, true);
        plot([x x], [7.16 6.6], 'Color', lc, 'LineWidth', 1.4);
        tt = linspace(0, 2*pi, 50);
        plot(x + 0.38*cos(tt), 6.25 + 0.38*sin(tt), 'Color', lc, 'LineWidth', 1.4);
        plot(x + 0.38*cos(tt), 5.75 + 0.38*sin(tt), 'Color', lc, 'LineWidth', 1.4);
        text(x + 0.5, 6.0, sprintf('T%d\n31.5 MVA', i), 'FontSize', 7.5);
        plot([x x], [5.37 4.9], 'Color', lc, 'LineWidth', 1.4);
        breaker(x, 4.62, true);
        plot([x x], [4.48 4.0], 'Color', lc, 'LineWidth', 1.4);
    end
    plot([1.5 5.8], [4 4], 'Color', lc, 'LineWidth', 3);
    plot([6.2 10.5], [4 4], 'Color', lc, 'LineWidth', 3);
    text(1.5, 4.25, 'Bus I (10 kV)', 'FontSize', 8);
    text(9.0, 4.25, 'Bus II (10 kV)', 'FontSize', 8);
    breaker(6.0, 4.0, false);
    text(6.0, 3.55, sprintf('bus tie\n(N.O.)'), 'FontSize', 7, 'HorizontalAlignment', 'center');
    feeders = [2.2 3.4 4.6 7.4 8.6 9.8];
    for x = feeders
        plot([x x], [4.0 3.2], 'Color', lc, 'LineWidth', 1.2);
        breaker(x, 2.95, true);
        q = quiver(x, 2.8, 0, -0.9, 0, 'Color', lc, 'LineWidth', 1.1, 'MaxHeadSize', 0.5);
        q.AutoScale = 'off';
    end
    text(6.0, 1.45, 'outgoing feeders (10 kV)', 'FontSize', 8, 'HorizontalAlignment', 'center');
    title('Single-line diagram (110/10 kV substation)');
end

function breaker(x, y, closed)
    if closed
        rectangle('Position', [x-0.14 y-0.14 0.28 0.28], ...
                  'FaceColor', [0.18 0.31 0.47], 'EdgeColor', [0.18 0.31 0.47], 'LineWidth', 1.2);
    else
        rectangle('Position', [x-0.14 y-0.14 0.28 0.28], ...
                  'FaceColor', 'w', 'EdgeColor', [0.77 0.31 0.32], 'LineWidth', 1.2);
    end
end
