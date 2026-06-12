function fig = bump_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    n_item = 6; n_per = 10;
    scores = cumsum(randn(n_item, n_per), 2);
    ranks = zeros(n_item, n_per);              % rank 1 = highest score
    for j = 1:n_per
        [~, ord] = sort(scores(:, j), 'descend');
        ranks(ord, j) = 1:n_item;
    end
    labels = {'Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot'};
    t_fine = linspace(0, n_per-1, 200);
    seg = min(max(floor(t_fine), 0), n_per-2);
    frac = t_fine - seg;
    ease = 3*frac.^2 - 2*frac.^3;              % smoothstep easing
    fig = figure('Position', [100 100 700 400]); hold on;
    for i = 1:n_item
        y = ranks(i, seg+1) + (ranks(i, seg+2) - ranks(i, seg+1)).*ease;
        c = palette('cat', i);
        plot(t_fine, y, 'Color', c, 'LineWidth', 2);
        plot(0:n_per-1, ranks(i, :), 'o', 'Color', c, 'MarkerFaceColor', c, ...
             'MarkerSize', 5);
        text(n_per-0.7, ranks(i, end), labels{i}, 'Color', c, 'FontSize', 8, ...
             'VerticalAlignment', 'middle');
    end
    xlim([-0.3, n_per+1.0]); ylim([0.5, n_item+0.5]);
    set(gca, 'YDir', 'reverse', 'YTick', 1:n_item, 'XTick', 0:n_per-1, ...
        'XTickLabel', arrayfun(@(q) sprintf('Q%d', q), 1:n_per, 'UniformOutput', false));
    xlabel('period'); ylabel('rank'); title('Ranking over time (bump chart)');
    ax = gca; ax.XGrid = 'on'; ax.YGrid = 'off';
end
