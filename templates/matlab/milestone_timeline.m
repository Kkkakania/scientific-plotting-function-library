function fig = milestone_timeline()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    x = [1 3 6 9 12 15 18];
    names = {'Kick-off', 'Spec freeze', 'Alpha build', 'Field test', ...
             'Beta release', 'Certification', 'Launch'};
    % alternate above/below the axis, with two stem heights to avoid overlap
    levels = [1 -1 0.6 -0.6 1 -1 0.6];
    fig = figure('Position', [100 100 800 350]); hold on;
    plot([0 19], [0 0], 'Color', [0.4 0.4 0.4], 'LineWidth', 1.2);
    for i = 1:numel(x)
        plot([x(i) x(i)], [0 levels(i)], 'Color', palette('cat',1), 'LineWidth', 1);
    end
    plot(x, zeros(size(x)), 'o', 'Color', palette('cat',2), 'MarkerSize', 7, ...
         'MarkerFaceColor', 'w', 'LineWidth', 1.6, 'LineStyle', 'none');
    for i = 1:numel(x)
        lv = levels(i);
        if lv > 0, va = 'bottom'; else, va = 'top'; end
        text(x(i), lv + 0.09*sign(lv), names{i}, 'HorizontalAlignment', 'center', ...
             'VerticalAlignment', va, 'FontSize', 8);
        if lv > 0, va2 = 'top'; else, va2 = 'bottom'; end
        text(x(i), -0.14*sign(lv), sprintf('M%d', x(i)), ...
             'HorizontalAlignment', 'center', 'VerticalAlignment', va2, ...
             'FontSize', 7, 'Color', [0.53 0.53 0.53]);
    end
    xlim([0 19]); ylim([-1.6 1.6]);
    set(gca, 'YTick', [], 'Box', 'off', 'YColor', 'none');
    xlabel('project month'); title('Milestone timeline');
end
