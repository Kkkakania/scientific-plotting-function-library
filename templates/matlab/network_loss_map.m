function fig = network_loss_map()
    % 电网网损分布 (IEEE-14 风格): 支路宽度=潮流, 颜色=损耗
    % 损耗近似 P_loss = r_pu * (P/Sbase)^2 * Sbase (V≈1 pu), Sbase=100 MVA
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    xy = [0 0.6; 2 0; 5 0; 4.4 1.5; 2.4 1.5; 2 2.8; 4.8 2.3; 6 2.3; ...
          4.4 3.2; 3.7 3.9; 2.8 3.5; 0.9 3.6; 2 4.3; 3.5 4.7];
    br = [1 2; 1 5; 2 3; 2 4; 2 5; 3 4; 4 5; 4 7; 4 9; 5 6; ...
          6 11; 6 12; 6 13; 7 8; 7 9; 9 10; 9 14; 10 11; 12 13; 13 14];
    r = [.01938 .05403 .04699 .05811 .05695 .06701 .01335 .002 .002 .002 ...
         .09498 .12291 .06615 .001 .001 .03181 .12711 .08205 .22092 .17093];
    flows = [157 75 73 56 42 23 61 28 16 44 7 8 18 21 28 5 9 4 2 6];
    gen = [1 2 3 6 8];
    sbase = 100;
    loss = r .* (flows/sbase).^2 * sbase;                    % MW
    lw = 0.8 + 4.0 * flows / max(flows);                     % 宽度 = 潮流
    cmap = palette('seq_orange');                            % 截掉最浅 20%
    cmap = cmap(round(0.2*size(cmap,1)):end, :);
    fig = figure('Position', [100 100 640 460]); hold on;
    for k = 1:size(br, 1)                                    % 20 条支路, 循环可接受
        ci = 1 + round((size(cmap,1)-1) * loss(k)/max(loss));
        plot(xy(br(k,:), 1), xy(br(k,:), 2), '-', ...
             'Color', cmap(ci, :), 'LineWidth', lw(k));
    end
    colormap(cmap); caxis([0 max(loss)]);
    cb = colorbar; cb.Label.String = 'branch loss (MW)';
    isgen = ismember(1:14, gen);
    hL = plot(xy(~isgen,1), xy(~isgen,2), 'o', 'MarkerSize', 9, ...
              'MarkerFaceColor', 'w', 'MarkerEdgeColor', palette('cat',1), ...
              'LineWidth', 1.4, 'LineStyle', 'none');
    hG = plot(xy(isgen,1), xy(isgen,2), 'o', 'MarkerSize', 9, ...
              'MarkerFaceColor', palette('cat',1), ...
              'MarkerEdgeColor', palette('cat',1), 'LineStyle', 'none');
    text(xy(:,1), xy(:,2) + 0.22, compose('%d', (1:14)'), ...
         'HorizontalAlignment', 'center', 'FontSize', 8);
    text(-0.4, -0.35, sprintf('total loss = %.1f MW', sum(loss)), 'FontSize', 8);
    axis equal; xlim([-0.5 6.6]); ylim([-0.5 5.2]); axis off;
    title('Network loss map (IEEE 14-bus style)');
    legend([hL hG], {'Load bus', 'Generator bus'}, ...
           'Location', 'northwest', 'Box', 'off', 'FontSize', 7);
end
