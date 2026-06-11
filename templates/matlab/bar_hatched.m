function fig = bar_hatched()
%BAR_HATCHED 带填充纹理的分组柱状图（黑白印刷友好；自绘纹理，不依赖外部工具）
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    % demo 数据：4 系列 x 5 组
    data = 2 + 7*rand(4, 5);
    [nser, ngrp] = size(data);
    width = 0.8/nser;
    styles = {'fwd', 'cross', 'vert', 'back'};   % 每系列一种纹理
    fig = figure;
    hold on;
    h = gobjects(1, nser);
    for i = 1:nser
        xc = (1:ngrp) + (i - (nser+1)/2)*width;
        h(i) = bar(xc, data(i, :), width, 'FaceColor', palette('cat', i), ...
                   'EdgeColor', 'k', 'LineWidth', 0.8);
        % 对每根柱叠加纹理线
        for j = 1:ngrp
            add_hatch(xc(j)-width/2, xc(j)+width/2, 0, data(i, j), ...
                      0.18, styles{mod(i-1, numel(styles))+1});
        end
    end
    hold off;
    xticks(1:ngrp); xticklabels(compose('S%d', 1:ngrp));
    xlabel('sample'); ylabel('RMSE (m)');
    title('Hatched grouped bars');
    ylim([0, 1.28*max(data(:))]);
    legend(h, compose('method %c', 'A'-1+(1:nser)), 'Box', 'off', ...
           'Orientation', 'horizontal', 'Location', 'north');
    set(gca, 'TickDir', 'out', 'YGrid', 'on', 'XGrid', 'off');
end

function add_hatch(x1, x2, y1, y2, sp, style)
%ADD_HATCH 在矩形 [x1,x2]x[y1,y2] 内画纹理线（NaN 分隔，单次 plot）
%   sp 为归一化间距（相对矩形宽度），style: fwd/back/cross/vert
    X = []; Y = [];
    if strcmp(style, 'fwd') || strcmp(style, 'cross')
        [xs, ys] = diag_seg(x1, x2, y1, y2, sp, +1);
        X = [X, xs]; Y = [Y, ys];
    end
    if strcmp(style, 'back') || strcmp(style, 'cross')
        [xs, ys] = diag_seg(x1, x2, y1, y2, sp, -1);
        X = [X, xs]; Y = [Y, ys];
    end
    if strcmp(style, 'vert')
        w = x2 - x1;
        xv = (x1+sp*w):(sp*w):(x2-sp*w/4);
        nv = numel(xv);
        X = [X, reshape([xv; xv; nan(1, nv)], 1, [])];
        Y = [Y, repmat([y1, y2, NaN], 1, nv)];
    end
    if ~isempty(X)
        plot(X, Y, 'k', 'LineWidth', 0.5, 'HandleVisibility', 'off');
    end
end

function [X, Y] = diag_seg(x1, x2, y1, y2, sp, sgn)
%DIAG_SEG 在归一化矩形 [0,1]^2 内生成 45 度线族 v = sgn*u + c，
%   裁剪后映射回数据坐标，返回 NaN 分隔的线段坐标
    w = x2 - x1; ht = y2 - y1;
    X = []; Y = [];
    if w <= 0 || ht <= 0
        return;
    end
    if sgn > 0
        crange = -1:sp:1;
    else
        crange = 0:sp:2;
    end
    for c = crange
        if sgn > 0
            ua = max(0, -c); ub = min(1, 1 - c);
        else
            ua = max(0, c - 1); ub = min(1, c);
        end
        if ub > ua + 1e-9
            va = sgn*ua + c; vb = sgn*ub + c;
            X = [X, x1+ua*w, x1+ub*w, NaN]; %#ok<AGROW>
            Y = [Y, y1+va*ht, y1+vb*ht, NaN]; %#ok<AGROW>
        end
    end
end
