function fig = roc_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    fig = figure; hold on;
    seps = [0.3 1.0 2.0];
    for i = 1:3
        sep = seps(i);
        pos = randn(300,1) + sep; neg = randn(300,1);
        scores = [pos; neg]; labels = [ones(300,1); zeros(300,1)];
        [~, idx] = sort(-scores); labels = labels(idx);
        tpr = cumsum(labels) / sum(labels);
        fpr = cumsum(1 - labels) / sum(1 - labels);
        auc = trapz(fpr, tpr);
        plot(fpr, tpr, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    plot([0 1], [0 1], '--', 'Color', [0.5 0.5 0.5]);
    xlabel('FPR'); ylabel('TPR'); title('ROC curves');
    legend(arrayfun(@(s)sprintf('sep=%.1f',s),seps,'UniformOutput',false));
    grid on;
end
