function fig = sankey_multistage()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    L1 = [20 10; 10 15; 5 10];          % sources -> mid
    L2 = [15 12 8; 10 10 15];           % mid -> sinks
    src = sum(L1, 2)'; mid = sum(L1, 1); snk = sum(L2, 1);
    gap = 4.0; w = 0.16;
    xs = [0.0 1.6 3.2];
    ys_s = stack_(src, gap); ys_m = stack_(mid, gap); ys_t = stack_(snk, gap);
    fig = figure('Position',[100 100 640 420]); hold on;
    % stage 1 bands
    off_o = ys_s(:, 2); off_i = ys_m(:, 2);
    for i = 1:3
        for j = 1:2
            v = L1(i, j);
            if v > 0
                band_(xs(1)+w, xs(2), off_o(i)-v, off_o(i), ...
                      off_i(j)-v, off_i(j), palette('cat',i));
                off_o(i) = off_o(i) - v; off_i(j) = off_i(j) - v;
            end
        end
    end
    % stage 2 bands
    off_o = ys_m(:, 2); off_i = ys_t(:, 2);
    for i = 1:2
        for j = 1:3
            v = L2(i, j);
            if v > 0
                band_(xs(2)+w, xs(3), off_o(i)-v, off_o(i), ...
                      off_i(j)-v, off_i(j), palette('cat',3+i));
                off_o(i) = off_o(i) - v; off_i(j) = off_i(j) - v;
            end
        end
    end
    % node rectangles + labels
    names = {{'S1','S2','S3'}, {'M1','M2'}, {'T1','T2','T3'}};
    allys = {ys_s, ys_m, ys_t};
    for s = 1:3
        ys = allys{s}; nm = names{s};
        for k = 1:size(ys, 1)
            if s == 1, c = palette('cat',k);
            elseif s == 2, c = palette('cat',3+k);
            else, c = [0.48 0.51 0.54];
            end
            patch('XData', xs(s)+[0 w w 0], ...
                  'YData', [ys(k,1) ys(k,1) ys(k,2) ys(k,2)], ...
                  'FaceColor', c, 'EdgeColor', 'none');
            text(xs(s)+w/2, mean(ys(k,:)), nm{k}, 'HorizontalAlignment', ...
                 'center', 'FontSize', 8, 'Color', [1 1 1]);
        end
    end
    xlim([-0.25 3.6]); axis off;
    title('Three-stage Sankey flow', 'FontSize', 11);
end

function band_(x0, x1, yb0, yt0, yb1, yt1, color)
    t = linspace(0, 1, 60);
    s = (1 - cos(pi*t)) / 2;
    x = x0 + (x1 - x0) * t;
    yb = yb0 + (yb1 - yb0) * s;
    yt = yt0 + (yt1 - yt0) * s;
    fill([x fliplr(x)], [yb fliplr(yt)], color, ...
         'FaceAlpha', 0.45, 'EdgeColor', 'none');
end

function ys = stack_(vals, gap)
    top = sum(vals) + gap * (numel(vals) - 1);
    ys = zeros(numel(vals), 2);
    y = top;
    for k = 1:numel(vals)
        ys(k, :) = [y - vals(k), y];
        y = y - vals(k) - gap;
    end
end
