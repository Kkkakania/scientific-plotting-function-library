function fig = flowchart_methodology()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position', [100 60 640 640]); hold on;
    axis([0 10 0 10]); axis off; daspect([1 1 1]);
    steps = {'Problem definition', 'oval'; 'Data acquisition', 'box';
             sprintf('Preprocessing &\nfeature extraction'), 'box';
             'Model training', 'box'; 'Validation & comparison', 'box';
             'Conclusions', 'oval'};
    ys = 9.2 - (0:5)*1.55; main = zeros(6, 4);
    for i = 1:6
        main(i, :) = mnode(5, ys(i), steps{i, 1}, steps{i, 2}, 3.2, 0.95);
        if i > 1, marrow(main(i-1, :), main(i, :)); end
    end
    s1 = mnode(1.6, ys(2), sprintf('Field\nmeasurements'), 'para', 2.2, 0.95);
    s2 = mnode(8.4, ys(2), sprintf('Simulation\ndataset'), 'para', 2.2, 0.95);
    marrow(s1, main(2, :)); marrow(s2, main(2, :));
    cr = mnode(8.4, ys(5) + 0.0, sprintf('Metrics:\nRMSE / MAE / R^2'), 'alt', 2.3, 0.95);
    marrow(cr, main(5, :));
    title('Research methodology');
end

function n = mnode(cx, cy, txt, kind, w, h)
    switch kind
        case 'oval'
            tt = linspace(0, 2*pi, 60);
            fill(cx + w/2*cos(tt), cy + h/2*sin(tt), [0.87 0.93 0.87], ...
                 'EdgeColor', [0.23 0.42 0.28], 'LineWidth', 1.2);
        case 'para'
            s = w*0.12;
            fill(cx + [-w/2+s w/2+s w/2-s -w/2-s], cy + [h/2 h/2 -h/2 -h/2], ...
                 [0.92 0.87 0.94], 'EdgeColor', [0.42 0.23 0.47], 'LineWidth', 1.2);
        case 'alt'
            rectangle('Position', [cx-w/2 cy-h/2 w h], 'Curvature', 0.15, ...
                      'FaceColor', [0.96 0.86 0.86], 'EdgeColor', [0.54 0.19 0.20], 'LineWidth', 1.2);
        otherwise
            rectangle('Position', [cx-w/2 cy-h/2 w h], 'Curvature', 0.15, ...
                      'FaceColor', [0.86 0.91 0.96], 'EdgeColor', [0.18 0.31 0.47], 'LineWidth', 1.2);
    end
    text(cx, cy, txt, 'HorizontalAlignment', 'center', 'FontSize', 8.5);
    n = [cx cy w h];
end

function marrow(src, dst)
    cxs = src(1); cys = src(2); cxd = dst(1); cyd = dst(2);
    if abs(cyd - cys) >= abs(cxd - cxs)
        p1 = [cxs cys - sign(cys - cyd)*src(4)/2*(-1)];
        p1 = [cxs cys + sign(cyd - cys)*src(4)/2];
        p2 = [cxd cyd + sign(cys - cyd)*dst(4)/2];
    else
        p1 = [cxs + sign(cxd - cxs)*src(3)/2 cys];
        p2 = [cxd + sign(cxs - cxd)*dst(3)/2 cyd];
    end
    q = quiver(p1(1), p1(2), p2(1)-p1(1), p2(2)-p1(2), 0, ...
           'Color', [0.25 0.25 0.25], 'LineWidth', 1.1, 'MaxHeadSize', 0.3);
    q.AutoScale = 'off';
end
