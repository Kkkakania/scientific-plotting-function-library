function fig = pie_donut()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % 合成数据：能源结构占比
    labels = {'Coal','Gas','Hydro','Wind','Solar','Nuclear'};
    values = [34 22 14 12 8 10] + 2*rand(1, 6) - 1;
    frac = values / sum(values);
    edges = [0 cumsum(frac)];
    r_in = 0.58; r_out = 1.0;
    fig = figure;
    hold on;
    for k = 1:numel(values)
        % 从正上方起顺时针扫过该扇区（环形 = 外弧 + 内弧回程的闭合 patch）
        th = linspace(pi/2 - 2*pi*edges(k), pi/2 - 2*pi*edges(k+1), 60);
        xs = [r_out*cos(th), r_in*cos(fliplr(th))];
        ys = [r_out*sin(th), r_in*sin(fliplr(th))];
        patch(xs, ys, palette('cat', k), 'EdgeColor', 'w', 'LineWidth', 1.2);
        mid = pi/2 - pi*(edges(k) + edges(k+1));
        rl = (r_in + r_out) / 2;
        text(rl*cos(mid), rl*sin(mid), sprintf('%.1f%%', 100*frac(k)), ...
            'HorizontalAlignment', 'center', 'Color', 'w', 'FontSize', 8);
        text(1.12*cos(mid), 1.12*sin(mid), labels{k}, 'FontSize', 9, ...
            'HorizontalAlignment', ha_for(mid));
    end
    text(0, 0, sprintf('total\n%.0f', sum(values)), ...
        'HorizontalAlignment', 'center', 'FontSize', 10);
    axis equal;
    axis off;
    title('Energy mix share');
    hold off;
end

function h = ha_for(ang)
    % 按角度决定标签靠左/靠右，避免压到环上
    c = cos(ang);
    if c > 0.2
        h = 'left';
    elseif c < -0.2
        h = 'right';
    else
        h = 'center';
    end
end
