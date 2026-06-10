function fig = multiclass_roc()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    n_per = 200; n_class = 4;
    scores = zeros(n_class*n_per, n_class);
    labels = repelem((0:n_class-1)', n_per);
    for k = 0:n_class-1
        for j = 0:n_class-1
            mu = 0; if j == k, mu = 1.5; end
            scores(labels == k, j+1) = randn(n_per, 1) + mu;
        end
    end
    fig = figure; hold on;
    for k = 0:n_class-1
        y = double(labels == k);
        [~, idx] = sort(-scores(:, k+1)); y = y(idx);
        tpr = cumsum(y) / sum(y);
        fpr = cumsum(1 - y) / sum(1 - y);
        plot(fpr, tpr, 'Color', palette('cat',k+1), 'LineWidth', 1.5);
    end
    plot([0 1],[0 1],'--','Color',[0.5 0.5 0.5]);
    xlabel('FPR'); ylabel('TPR'); title('Multi-class ROC (OvR)');
    legend(arrayfun(@(k)sprintf('class %d',k), 0:n_class-1, 'UniformOutput', false));
    grid on;
end
