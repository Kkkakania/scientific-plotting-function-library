function fig = scatter_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    k = 3; names = {'V1', 'V2', 'V3'};
    L = [1 .6 .2; 0 1 .5; 0 0 1];
    A = (randn(80, k) .* [1 .8 1.2]) * L;
    B = [2.5 2 1] + randn(80, k) .* [1 .9 .8];
    data = {A, B};
    fig = figure('Position', [100 80 640 600]);
    for i = 1:k
        for j = 1:k
            subplot(k, k, (i-1)*k + j); hold on;
            for g = 1:2
                d = data{g};
                if i == j
                    histogram(d(:, j), 15, 'FaceColor', palette('cat', g), ...
                              'FaceAlpha', 0.55, 'EdgeColor', 'none');
                else
                    scatter(d(:, j), d(:, i), 8, palette('cat', g), 'filled', ...
                            'MarkerFaceAlpha', 0.6);
                end
            end
            if i == k, xlabel(names{j}); end
            if j == 1, ylabel(names{i}); end
            set(gca, 'FontSize', 7); grid on;
        end
    end
    sgtitle('Scatter-plot matrix', 'FontSize', 11);
end
