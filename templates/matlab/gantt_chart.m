function fig = gantt_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % task name, start day, duration, fraction complete, predecessor (0 = none)
    names = {'Requirements', 'System design', 'Prototype', 'Procurement', ...
             'Implementation', 'Integration', 'Validation', 'Documentation'};
    s    = [ 0  8 18 14 30 44 52 40];
    d    = [10 12 14 18 20 12 14 24];
    frac = [1.00 1.00 0.80 0.65 0.35 0.10 0.00 0.20];
    dep  = [0 1 2 2 3 5 6 4];
    today = 38; n = numel(names);
    gray = [0.47 0.47 0.47];
    fig = figure('Position', [100 100 800 420]); hold on;
    for i = 1:n
        c = palette('cat', mod(i-1, 4) + 1);
        fill([s(i) s(i)+d(i) s(i)+d(i) s(i)], [i-0.275 i-0.275 i+0.275 i+0.275], ...
             c, 'FaceAlpha', 0.30, 'EdgeColor', 'none');
        if frac(i) > 0                        % completed portion (solid)
            w = d(i)*frac(i);
            fill([s(i) s(i)+w s(i)+w s(i)], [i-0.275 i-0.275 i+0.275 i+0.275], ...
                 c, 'EdgeColor', 'none');
        end
        text(s(i) + d(i) + 0.6, i, sprintf('%.0f%%', frac(i)*100), 'FontSize', 7);
        if dep(i) > 0                         % dependency elbow arrow
            p = dep(i); xe = s(p) + d(p);
            plot([xe s(i) s(i)], [p p i-0.42], 'Color', gray, 'LineWidth', 0.9);
            plot(s(i), i-0.42, 'v', 'Color', gray, 'MarkerFaceColor', gray, ...
                 'MarkerSize', 3);
        end
    end
    plot([today today], [0.4 n+0.6], '--', 'Color', palette('cat',2), 'LineWidth', 1.2);
    text(today, 0.55, ' today', 'Color', palette('cat',2), 'FontSize', 8);
    set(gca, 'YDir', 'reverse', 'YTick', 1:n, 'YTickLabel', names);
    ylim([0.4 n+0.6]); xlim([-1 80]);
    xlabel('project day'); ylabel('task'); title('Project Gantt chart');
    grid on; set(gca, 'YGrid', 'off');
end
