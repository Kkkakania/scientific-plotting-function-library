function fig = flowchart_algorithm()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position', [100 60 560 700]); hold on;
    axis([0 9 0 11]); axis off; daspect([1 1 1]);
    s  = fnode(4.5, 10.2, 'Start', 'oval', 2.0, 0.9);
    a  = fnode(4.5, 8.8, sprintf('Initialize population\nk = 0'), 'box', 2.6, 0.95);
    b  = fnode(4.5, 7.4, 'Evaluate fitness', 'box', 2.6, 0.9);
    c  = fnode(4.5, 5.8, 'Converged?', 'diamond', 2.6, 0.9);
    d  = fnode(4.5, 4.0, sprintf('Selection / crossover\nmutation, k = k+1'), 'box', 2.8, 1.0);
    e  = fnode(4.5, 2.4, 'Output best solution', 'para', 2.8, 0.9);
    f  = fnode(4.5, 1.0, 'End', 'oval', 2.0, 0.9);
    farrow(s, a, ''); farrow(a, b, ''); farrow(b, c, '');
    farrow(c, d, 'No');
    fpoly([4.5-1.4 4.0; 1.6 4.0; 1.6 7.4; 4.5-1.3 7.4]);   % 循环回边
    farrow(c, e, 'Yes', [7.6 5.8; 7.6 2.4]);
    farrow(e, f, '');
    title('Algorithm flowchart');
end

function n = fnode(cx, cy, txt, kind, w, h)
    col = struct('box', {{[0.86 0.91 0.96], [0.18 0.31 0.47]}}, ...
                 'oval', {{[0.87 0.93 0.87], [0.23 0.42 0.28]}}, ...
                 'diamond', {{[0.98 0.93 0.83], [0.66 0.45 0.10]}}, ...
                 'para', {{[0.92 0.87 0.94], [0.42 0.23 0.47]}});
    cc = col.(kind);
    switch kind
        case 'oval'
            tt = linspace(0, 2*pi, 60);
            fill(cx + w/2*cos(tt), cy + h/2*sin(tt), cc{1}, 'EdgeColor', cc{2}, 'LineWidth', 1.2);
        case 'diamond'
            fill(cx + [0 w*0.62 0 -w*0.62], cy + [h*0.75 0 -h*0.75 0], cc{1}, ...
                 'EdgeColor', cc{2}, 'LineWidth', 1.2);
            h = h*1.5;
        case 'para'
            sft = w*0.12;
            fill(cx + [-w/2+sft w/2+sft w/2-sft -w/2-sft], cy + [h/2 h/2 -h/2 -h/2], ...
                 cc{1}, 'EdgeColor', cc{2}, 'LineWidth', 1.2);
        otherwise
            rectangle('Position', [cx-w/2 cy-h/2 w h], 'Curvature', 0.15, ...
                      'FaceColor', cc{1}, 'EdgeColor', cc{2}, 'LineWidth', 1.2);
    end
    text(cx, cy, txt, 'HorizontalAlignment', 'center', 'FontSize', 8.5);
    n = [cx cy w h];
end

function farrow(src, dst, lab, via)
    if nargin < 4, via = []; end
    if isempty(via)
        p1 = anchor(src, dst(1:2)); p2 = anchor(dst, src(1:2));
        pts = [p1; p2];
    else
        p1 = anchor(src, via(1, :)); p2 = anchor(dst, via(end, :));
        pts = [p1; via; p2];
    end
    for i = 1:size(pts, 1)-1
        if i == size(pts, 1)-1
            q = quiver(pts(i,1), pts(i,2), pts(i+1,1)-pts(i,1), pts(i+1,2)-pts(i,2), 0, ...
                   'Color', [0.25 0.25 0.25], 'LineWidth', 1.1, 'MaxHeadSize', 0.35);
            q.AutoScale = 'off';
        else
            plot([pts(i,1) pts(i+1,1)], [pts(i,2) pts(i+1,2)], ...
                 'Color', [0.25 0.25 0.25], 'LineWidth', 1.1);
        end
    end
    if ~isempty(lab)
        text((pts(1,1)+pts(end,1))/2 + 0.15, (pts(1,2)+pts(end,2))/2 + 0.12, lab, 'FontSize', 8);
    end
end

function fpoly(pts)
    plot(pts(:,1), pts(:,2), 'Color', [0.25 0.25 0.25], 'LineWidth', 1.1);
    q = quiver(pts(end,1), pts(end,2), 0.25, 0, 0, 'Color', [0.25 0.25 0.25], ...
           'LineWidth', 1.1, 'MaxHeadSize', 0.8);
    q.AutoScale = 'off';
end

function p = anchor(node, target)
    cx = node(1); cy = node(2); w = node(3); h = node(4);
    if abs(target(2) - cy) >= abs(target(1) - cx)
        if target(2) > cy, p = [cx cy + h/2]; else, p = [cx cy - h/2]; end
    else
        if target(1) > cx, p = [cx + w/2 cy]; else, p = [cx - w/2 cy]; end
    end
end
