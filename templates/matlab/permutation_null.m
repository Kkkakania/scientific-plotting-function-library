function fig = permutation_null()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    n_perm = 5000;
    x = randn(1, 40);
    y = 0.8 + randn(1, 35);
    obs = mean(y) - mean(x);
    pooled = [x y];
    nx = numel(x); N = numel(pooled);
    null_v = zeros(1, n_perm);
    for p = 1:n_perm
        idx = randperm(N);
        null_v(p) = mean(pooled(idx(nx+1:end))) - mean(pooled(idx(1:nx)));
    end
    pval = mean(abs(null_v) >= abs(obs));
    [counts, edges] = histcounts(null_v, 50);     % manual histogram, no toolbox
    centers = (edges(1:end-1) + edges(2:end))/2;
    tail = abs(centers) >= abs(obs);
    fig = figure; hold on;
    bar(centers, counts.*(~tail), 1, 'FaceColor', palette('cat',1), ...
        'FaceAlpha', 0.7, 'EdgeColor', 'w', 'LineWidth', 0.3);
    bar(centers, counts.*tail, 1, 'FaceColor', palette('cat',2), ...
        'FaceAlpha', 0.9, 'EdgeColor', 'w', 'LineWidth', 0.3);
    ym = max(counts)*1.05;
    hob = plot([obs obs], [0 ym], 'k-', 'LineWidth', 1.4);
    plot([-obs -obs], [0 ym], 'k:', 'LineWidth', 1.0);
    text(0.02, 0.95, sprintf('two-sided p = %.4f\n(%d permutations)', pval, n_perm), ...
         'Units', 'normalized', 'VerticalAlignment', 'top', 'FontSize', 8);
    ylim([0 ym]);
    xlabel('mean difference under null'); ylabel('count');
    title('Permutation test null distribution');
    legend(hob, {sprintf('observed diff = %.2f', obs)}, 'Location', 'northeast');
    grid on; set(gca, 'XGrid', 'off');
end
