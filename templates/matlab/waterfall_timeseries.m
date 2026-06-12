function fig = waterfall_timeseries()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(24);
    months = {'Jan','Feb','Mar','Apr','May','Jun', ...
              'Jul','Aug','Sep','Oct','Nov','Dec'};
    start = 120.0;
    delta = round(2 + 8 * randn(1, 12), 1);
    fin = start + sum(delta);
    labels = [{'Start'} months {'End'}];
    x = 0:13;
    bottoms = start + [0 cumsum(delta)];      % running level, length 13
    c_tot = palette('cat',8); c_up = palette('cat',3); c_dn = palette('cat',2);
    hw = 0.325;
    fig = figure('Position',[100 100 800 400]); hold on;
    patch('XData', [-hw hw hw -hw], 'YData', [0 0 start start], ...
          'FaceColor', c_tot, 'EdgeColor', 'none');
    for i = 1:12
        if delta(i) >= 0, c = c_up; else, c = c_dn; end
        y0 = bottoms(i); y1 = bottoms(i+1);
        patch('XData', i + [-hw hw hw -hw], 'YData', [y0 y0 y1 y1], ...
              'FaceColor', c, 'EdgeColor', 'none');
    end
    patch('XData', 13 + [-hw hw hw -hw], 'YData', [0 0 fin fin], ...
          'FaceColor', c_tot, 'EdgeColor', 'none');
    % step connector lines
    lv = [start bottoms(2:end) fin];
    for i = 1:13
        plot([x(i)-hw x(i+1)+hw], [lv(i) lv(i)], ':', ...
             'Color', [0.53 0.53 0.53], 'LineWidth', 0.7);
    end
    text(0, start + 1.5, sprintf('%.0f', start), 'HorizontalAlignment', ...
         'center', 'FontSize', 7);
    text(13, fin + 1.5, sprintf('%.0f', fin), 'HorizontalAlignment', ...
         'center', 'FontSize', 7);
    set(gca, 'XTick', x, 'XTickLabel', labels, 'XTickLabelRotation', 45, ...
        'FontSize', 7);
    xlim([-0.8 13.8]);
    xlabel('period'); ylabel('balance');
    title('Year-to-date waterfall bridge');
    hu = patch('XData', nan, 'YData', nan, 'FaceColor', c_up, 'EdgeColor', 'none');
    hd = patch('XData', nan, 'YData', nan, 'FaceColor', c_dn, 'EdgeColor', 'none');
    ht = patch('XData', nan, 'YData', nan, 'FaceColor', c_tot, 'EdgeColor', 'none');
    legend([hu hd ht], {'increase', 'decrease', 'total'}, ...
           'FontSize', 8, 'Box', 'off');
    set(gca, 'XGrid', 'off', 'YGrid', 'on');
end
