function fig = biplot_pca()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    n_feat = 6;
    centers = -2 + 4*rand(3, n_feat);
    X = []; labels = [];
    for k = 1:3
        X = [X; randn(40, n_feat)*0.7 + centers(k, :)];
        labels = [labels; k*ones(40, 1)];
    end
    Xc = X - mean(X, 1);
    [U, S, Vt] = svd(Xc, 'econ');
    PC = U(:, 1:2) * S(1:2, 1:2);
    loadings = Vt(:, 1:2) * S(1:2, 1:2) / sqrt(size(X, 1));
    fig = figure('Position',[100 100 700 600]); hold on;
    for k = 1:3
        m = labels == k;
        scatter(PC(m, 1), PC(m, 2), 30, palette('cat',k), 'filled', ...
                'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w');
    end
    sc = std(PC(:)) / std(loadings(:)) * 1.2;
    for i = 1:n_feat
        quiver(0, 0, loadings(i, 1)*sc, loadings(i, 2)*sc, 0, 'Color', 'r', 'LineWidth', 1.2);
        text(loadings(i, 1)*sc*1.1, loadings(i, 2)*sc*1.1, sprintf('f%d', i), 'Color', 'r');
    end
    xlabel('PC1'); ylabel('PC2'); title('PCA biplot');
    legend({'class 1','class 2','class 3'}); grid on;
end
