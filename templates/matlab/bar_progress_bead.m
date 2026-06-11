function fig = bar_progress_bead()
%BAR_PROGRESS_BEAD 滑珠进度柱状图：灰底100%柱 + 进度柱 + 顶端滑珠
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    % demo 数据
    total = 100;
    vals = sort(20 + 75*rand(1, 12), 'descend');
    vals = round(vals);
    x = 1:numel(vals);
    c = palette('cat', 1);
    fig = figure;
    hold on;
    % 背景 100% 轨道柱
    bar(x, total*ones(size(x)), 0.55, 'FaceColor', [0.90 0.90 0.90], ...
        'EdgeColor', 'none');
    % 前景进度柱
    bar(x, vals, 0.55, 'FaceColor', c, 'EdgeColor', 'none');
    % 顶端滑珠：白面 + 主题色描边
    scatter(x, vals, 70, 'filled', 'MarkerFaceColor', 'w', ...
            'MarkerEdgeColor', c, 'LineWidth', 1.6);
    % 数值标注
    text(x, vals + 0.045*total, string(vals), 'HorizontalAlignment', 'center', ...
         'FontSize', 8, 'Color', [0.25 0.25 0.25]);
    hold off;
    xticks(x);
    xticklabels(compose('M%d', x));
    xlabel('task'); ylabel('completion (%)');
    title('Progress bar with bead markers');
    ylim([0, 1.12*total]);
    set(gca, 'Box', 'off', 'TickDir', 'out', 'YGrid', 'on', 'XGrid', 'off');
end
