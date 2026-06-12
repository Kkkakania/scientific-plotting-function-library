function fig = arc_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    n = 12; n_edges = 16;
    x = 1:n;
    edges = zeros(0, 2);
    while size(edges, 1) < n_edges
        ij = sort(randperm(n, 2));
        if ~any(edges(:, 1) == ij(1) & edges(:, 2) == ij(2))
            edges(end+1, :) = ij; %#ok<AGROW>
        end
    end
    edges = sortrows(edges);
    fig = figure('Position', [100 100 640 400]); hold on;
    th = linspace(0, pi, 60);
    for e = 1:n_edges
        i = edges(e, 1); j = edges(e, 2);
        w = 0.5 + 2.0*rand;
        c = (x(i) + x(j))/2;
        r = (x(j) - x(i))/2;       % arc height = half the node distance
        plot(c + r*cos(th), r*sin(th), 'Color', [0.376 0.439 0.502 0.55], ...
             'LineWidth', 0.6 + 0.6*w);
    end
    plot([x(1)-0.4, x(end)+0.4], [0 0], 'Color', [0.690 0.714 0.737], 'LineWidth', 1);
    cols = zeros(n, 3);
    for k = 1:n, cols(k, :) = palette('cat', k); end
    scatter(x, zeros(1, n), 120, cols, 'filled', 'MarkerEdgeColor', 'w', 'LineWidth', 0.8);
    for k = 1:n
        text(x(k), -0.55, char(64+k), 'HorizontalAlignment', 'center', ...
             'VerticalAlignment', 'top', 'FontSize', 9);
    end
    xlim([0 n+1]); ylim([-1.2, n/2+0.6]);
    axis equal; axis off;
    title('Arc diagram', 'FontSize', 11);
end
