function fig = bar_overlay_mckinsey()
%BAR_OVERLAY_MCKINSEY 麦肯锡商务风叠加柱状图：同基线宽灰底柱 + 窄彩色柱
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % demo 数据
    refv = [72 65 58 47 39];               % 宽柱：对照组（底层）
    mainv = [88 71 75 52 33];              % 窄柱：重点组（顶层）
    labels = {'Data architecture', 'Cloud platforms', 'Advanced analytics', ...
              'Process automation', 'Digital talent'};
    n = numel(refv);
    y = 1:n;
    cmain = palette('cat', 1);
    cref = [0.82 0.82 0.82];
    fig = figure;
    hold on;
    % 同一基线两层 barh：宽灰底 + 窄彩色，形成"叠加"对比而非堆叠
    h1 = barh(y, refv, 0.72, 'FaceColor', cref, 'EdgeColor', 'none', ...
              'ShowBaseLine', 'off');
    h2 = barh(y, mainv, 0.34, 'FaceColor', cmain, 'EdgeColor', 'none', ...
              'ShowBaseLine', 'off');
    % 数值长在柱端内侧
    text(refv - 1.5, y - 0.26, string(refv), 'HorizontalAlignment', 'right', ...
         'FontSize', 9, 'Color', [0.35 0.35 0.35]);
    text(mainv - 1.5, y, string(mainv), 'HorizontalAlignment', 'right', ...
         'FontSize', 9, 'Color', 'w', 'FontWeight', 'bold');
    % 类目标签代替 y 轴
    text(-2.5*ones(1, n), y, labels, 'HorizontalAlignment', 'right', ...
         'FontSize', 9);
    % 标题与脚注
    text(-36, 0.1, 'Capabilities organizations invested in', ...
         'FontSize', 11, 'FontWeight', 'bold');
    text(0, n + 0.62, 'share of respondents (%)', 'FontSize', 8, ...
         'Color', [0.45 0.45 0.45]);
    hold off;
    set(gca, 'YDir', 'reverse', 'XLim', [-38 100], 'YLim', [-0.2 n+0.8]);
    axis off;
    lg = legend([h1, h2], {'All other respondents', 'Top performers'}, ...
                'Orientation', 'horizontal', 'Box', 'off', ...
                'Location', 'northwest');
    lg.ItemTokenSize = [8 8];              % 缩小图例色块（Nature/麦肯锡风）
end
