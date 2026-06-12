function fig = roc_multi_compare()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    n = 400;
    y = double((1:n)' <= n/2);                       % first half positives
    names = {'Model A', 'Model B', 'Model C', 'Model D'};
    seps = [2.0 1.4 0.9 0.45];
    fig = figure('Position',[100 100 500 460]); hold on;
    hs = gobjects(1, 4); labels = cell(1, 4);
    for i = 1:4
        score = randn(n, 1) + seps(i) * y;
        [~, order] = sort(score, 'descend');
        ys = y(order);
        tpr = [0; cumsum(ys) / sum(ys)];
        fpr = [0; cumsum(1 - ys) / (n - sum(ys))];
        auc = trapz(fpr, tpr);
        hs(i) = plot(fpr, tpr, 'Color', palette('cat',i), 'LineWidth', 1.5);
        labels{i} = sprintf('%s (AUC = %.3f)', names{i}, auc);
    end
    hchance = plot([0 1], [0 1], '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
    xlim([-0.02 1.02]); ylim([-0.02 1.02]);
    xlabel('false positive rate'); ylabel('true positive rate');
    title('ROC comparison');
    legend([hs hchance], [labels {'chance'}], 'Location', 'southeast');
    grid on;
end
