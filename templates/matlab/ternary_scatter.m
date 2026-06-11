function fig = ternary_scatter()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % 合成数据：合金成分（Dirichlet 抽样 = 归一化 gamma），a+b+c=1
    g = randg(repmat([2.5 1.8 1.2], 120, 1));
    abc = g ./ sum(g, 2);
    hv = 200 + 300*abc(:,1) - 120*abc(:,3) + 12*randn(120, 1);
    % 重心坐标 → 平面：A=(0,0) B=(1,0) C=(0.5, sqrt(3)/2)
    s32 = sqrt(3)/2;
    x = abc(:,2) + 0.5*abc(:,3);
    y = s32 * abc(:,3);
    fig = figure;
    hold on;
    % 三角形边框
    plot([0 1 0.5 0], [0 0 s32 0], 'Color', [0.25 0.25 0.25], 'LineWidth', 1.0);
    % 网格：三族等值线（每 20%）+ 底边刻度
    for f = 0.2:0.2:0.8
        gg = 1 - f;
        seg = [tern2xy(f, gg, 0), tern2xy(f, 0, gg); ...   % a = f
               tern2xy(gg, f, 0), tern2xy(0, f, gg); ...   % b = f
               tern2xy(gg, 0, f), tern2xy(0, gg, f)];      % c = f
        for j = 1:3
            plot(seg(j, [1 3]), seg(j, [2 4]), ':', ...
                'Color', [0.75 0.75 0.75], 'LineWidth', 0.6);
        end
        p = tern2xy(f, gg, 0);
        text(p(1), p(2)-0.03, sprintf('%.1f', f), 'FontSize', 7, ...
            'HorizontalAlignment', 'center', 'Color', [0.4 0.4 0.4]);
    end
    % 数据点（颜色映射硬度）
    scatter(x, y, 24, hv, 'filled', 'MarkerEdgeColor', [0.3 0.3 0.3], 'LineWidth', 0.3);
    colormap(palette('seq_blue', 256));
    cb = colorbar;
    cb.Label.String = 'hardness (HV)';
    % 顶点标签
    text(-0.04, -0.03, 'Cu', 'HorizontalAlignment', 'right', 'FontSize', 10);
    text(1.04, -0.03, 'Zn', 'HorizontalAlignment', 'left', 'FontSize', 10);
    text(0.5, s32+0.05, 'Ni', 'HorizontalAlignment', 'center', 'FontSize', 10);
    axis equal;
    axis off;
    xlim([-0.12 1.12]); ylim([-0.12 s32+0.12]);
    title('Ternary composition diagram');
    hold off;
end

function p = tern2xy(a, b, c)
    % 重心坐标 (a,b,c) → [x y]
    s = a + b + c;
    p = [(b + 0.5*c)/s, sqrt(3)/2 * c/s];
end
