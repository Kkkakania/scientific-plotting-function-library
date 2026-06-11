function fig = treemap_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % 合成数据：科研经费分项（squarify 算法要求降序）
    labels = {'Materials','Equipment','Personnel','Computing', ...
              'Travel','Publication','Outreach','Misc'};
    sizes = sort(10 + 90*rand(1, 8), 'descend');
    rects = squarify(sizes, 0, 0, 100, 100);
    total = sum(sizes);
    fig = figure;
    hold on;
    for k = 1:numel(sizes)
        r = rects(k, :);
        rectangle('Position', r, 'FaceColor', palette('cat', k), ...
            'EdgeColor', 'w', 'LineWidth', 1.5);
        if r(3)*r(4) > 250    % 太小的块不放文字
            text(r(1)+r(3)/2, r(2)+r(4)/2, ...
                sprintf('%s\n%.1f%%', labels{k}, 100*sizes(k)/total), ...
                'HorizontalAlignment', 'center', 'Color', 'w', 'FontSize', 8);
        end
    end
    axis([0 100 0 100]);
    axis equal;
    axis off;
    set(gca, 'YDir', 'reverse');
    title('Research budget treemap');
    hold off;
end

function rects = squarify(sizes, x, y, w, h)
    % squarified treemap：贪心按行铺设，纵横比一变差就固化当前行
    areas = sizes * (w*h) / sum(sizes);
    rects = zeros(numel(areas), 4);
    n = 0;
    row = [];
    while ~isempty(areas)
        side = min(w, h);
        cand = [row, areas(1)];
        if isempty(row) || worst_ratio(cand, side) <= worst_ratio(row, side)
            row = cand;
            areas(1) = [];
        else
            [placed, x, y, w, h] = layout_row(row, x, y, w, h);
            rects(n+1:n+size(placed,1), :) = placed;
            n = n + size(placed, 1);
            row = [];
        end
    end
    if ~isempty(row)
        placed = layout_row(row, x, y, w, h);
        rects(n+1:n+size(placed,1), :) = placed;
    end
end

function r = worst_ratio(areas, side)
    % 该行铺在长度 side 的短边上时的最差纵横比
    thick = sum(areas) / side;
    len = areas / thick;
    r = max(max(thick./len, len./thick));
end

function [placed, x2, y2, w2, h2] = layout_row(areas, x, y, w, h)
    % 把一行矩形铺进 (x,y,w,h) 的短边方向，返回矩形 Nx4 与剩余区域
    total = sum(areas);
    n = numel(areas);
    placed = zeros(n, 4);
    if w >= h               % 竖排成一列
        cw = total / h;
        cy = y;
        for i = 1:n
            placed(i, :) = [x, cy, cw, areas(i)/cw];
            cy = cy + areas(i)/cw;
        end
        x2 = x + cw; y2 = y; w2 = w - cw; h2 = h;
    else                    % 横排成一行
        rh = total / w;
        cx = x;
        for i = 1:n
            placed(i, :) = [cx, y, areas(i)/rh, rh];
            cx = cx + areas(i)/rh;
        end
        x2 = x; y2 = y + rh; w2 = w; h2 = h - rh;
    end
end
