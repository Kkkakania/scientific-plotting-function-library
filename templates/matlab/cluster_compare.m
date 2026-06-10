function fig = cluster_compare()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    n = 80;
    X = [randn(n, 2)*0.6 + [0 0];
         randn(n, 2)*0.6 + [3 3];
         randn(n, 2)*0.6 + [-3 3]];
    truth = repelem((1:3)', n);
    % KMeans
    centers = -3 + 6*rand(3, 2);
    for it = 1:10
        d = pdist2(X, centers); [~, lab_k] = min(d, [], 2);
        for k = 1:3
            centers(k, :) = mean(X(lab_k == k, :), 1);
        end
    end
    % Hierarchical
    Z = linkage(X, 'ward'); lab_h = cluster(Z, 'maxclust', 3);
    fig = figure('Position',[100 100 900 350]);
    labs = {truth, lab_k, lab_h}; names = {'Truth','K-Means','Hierarchical'};
    for s = 1:3
        subplot(1, 3, s); hold on;
        for k = 1:3
            m = labs{s} == k;
            scatter(X(m,1), X(m,2), 15, palette('cat',k), 'filled', 'MarkerFaceAlpha', 0.7);
        end
        title(names{s}); axis equal; grid on;
    end
    sgtitle('Clustering comparison');
end
