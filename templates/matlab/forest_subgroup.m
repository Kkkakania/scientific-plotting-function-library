function fig = forest_subgroup()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    groups = {'Trial set A','Trial set B','Trial set C'};
    n_per = 4;
    fig = figure('Position',[100 100 700 500]); hold on;
    y = 0; ticks = []; labels = {};
    for g = 1:3
        text(-2.3, y+0.5, groups{g}, 'FontWeight','bold');
        for s = 1:n_per
            y = y - 1;
            eff = 0.3 + 0.4*randn; err = 0.2 + 0.3*rand;
            plot([eff-err eff+err], [y y], 'Color', [0.5 0.5 0.5], 'LineWidth', 1.2);
            plot(eff, y, 's', 'Color', palette('cat',g), 'MarkerFaceColor', palette('cat',g), 'MarkerSize', 8);
            ticks(end+1) = y; labels{end+1} = sprintf('  study %d', s);
        end
        y = y - 1;
        plot(0.3, y, 'd', 'Color', palette('cat',g), 'MarkerFaceColor', palette('cat',g), 'MarkerSize', 10);
        ticks(end+1) = y; labels{end+1} = '  pooled';
        y = y - 0.5;
    end
    xline(0, 'k');
    set(gca,'YTick',sort(ticks),'YTickLabel',flip(labels));
    xlabel('effect size'); title('Subgroup forest plot'); grid on;
end
