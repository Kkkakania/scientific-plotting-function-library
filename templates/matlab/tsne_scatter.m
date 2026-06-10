function fig = tsne_scatter()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    centers = -4 + 8*rand(4, 8);
    X = []; labels = [];
    for k = 1:4
        X = [X; randn(60, 8)*0.6 + centers(k, :)];
        labels = [labels; (k-1)*ones(60, 1)];
    end
    Xc = X - mean(X, 1);
    [~, ~, V] = svd(Xc, 'econ');
    proj = Xc * V(:, 1:2);
    fig = figure;
    hold on;
    for k = 0:3
        m = labels == k;
        scatter(proj(m, 1), proj(m, 2), 30, palette('cat',k+1), 'filled', ...
                'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w');
    end
    xlabel('dim 1'); ylabel('dim 2'); title('2D embedding scatter');
    legend({'class 0','class 1','class 2','class 3'}); grid on;
end
