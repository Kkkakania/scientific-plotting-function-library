function fig = graph_directed()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    n = 8;
    ang = linspace(0, 2*pi, n+1) + pi/2; ang(end) = [];
    pos = 3*[cos(ang)' sin(ang)'];
    fig = figure('Position', [100 80 540 520]); hold on;
    axis([-4 4 -4 4]); axis off; daspect([1 1 1]);
    deg = zeros(1, n);
    for i = 1:n
        for j = 1:n
            if i ~= j && rand < 0.22
                w = 0.5 + 2.5*rand;
                t = linspace(0, 1, 40);
                mx = (pos(i,1)+pos(j,1))/2 - (pos(j,2)-pos(i,2))*0.12;
                my = (pos(i,2)+pos(j,2))/2 + (pos(j,1)-pos(i,1))*0.12;
                bx = (1-t).^2*pos(i,1) + 2*(1-t).*t*mx + t.^2*pos(j,1);
                by = (1-t).^2*pos(i,2) + 2*(1-t).*t*my + t.^2*pos(j,2);
                plot(bx(4:33), by(4:33), 'Color', [0.38 0.44 0.50 0.65], ...
                     'LineWidth', 0.5 + w*0.7);
                q = quiver(bx(33), by(33), bx(36)-bx(33), by(36)-by(33), 0, ...
                       'Color', [0.38 0.44 0.50], 'LineWidth', 1, 'MaxHeadSize', 8);
                q.AutoScale = 'off';
                deg(i) = deg(i) + 1; deg(j) = deg(j) + 1;
            end
        end
    end
    for k = 1:n
        ms = 16 + deg(k)*1.5;
        plot(pos(k,1), pos(k,2), 'o', 'MarkerSize', ms, ...
             'MarkerFaceColor', palette('cat', k), 'MarkerEdgeColor', 'none');
        text(pos(k,1), pos(k,2), num2str(k), 'Color', 'w', ...
             'HorizontalAlignment', 'center', 'FontSize', 9);
    end
    title('Weighted directed graph');
end
