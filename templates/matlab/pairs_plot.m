function fig = pairs_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    n = 4; data = randn(150, n);
    data(:, 2) = 0.7*data(:, 1) + 0.3*data(:, 2);
    data(:, 4) = -0.5*data(:, 3) + 0.5*data(:, 4);
    fig = figure('Position',[100 100 700 700]);
    for i = 1:n
        for j = 1:n
            subplot(n, n, (i-1)*n + j);
            if i == j
                histogram(data(:, i), 20, 'FaceColor', palette('cat',1), 'EdgeColor','w');
            else
                scatter(data(:, j), data(:, i), 6, palette('cat',1), 'filled', 'MarkerFaceAlpha', 0.5);
            end
            if i < n, set(gca,'XTickLabel',[]); end
            if j > 1, set(gca,'YTickLabel',[]); end
            if i == n, xlabel(sprintf('x%d', j), 'FontSize', 7); end
            if j == 1, ylabel(sprintf('x%d', i), 'FontSize', 7); end
        end
    end
    sgtitle('Pairs plot');
end
