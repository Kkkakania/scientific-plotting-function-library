function fig = graph_undirected()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    centers = [0 0; 4.2 1.2; 2.0 4.0]; k = 8;
    pos = []; com = [];
    for c = 1:3
        pos = [pos; centers(c, :) + 0.85*randn(k, 2)]; %#ok<AGROW>
        com = [com; c*ones(k, 1)]; %#ok<AGROW>
    end
    n = size(pos, 1);
    fig = figure('Position', [100 80 600 500]); hold on; axis off; daspect([1 1 1]);
    for i = 1:n
        for j = i+1:n
            if com(i) == com(j), p = 0.42; lw = 1.4; else, p = 0.03; lw = 0.7; end
            if rand < p
                plot(pos([i j], 1), pos([i j], 2), 'Color', [0.56 0.63 0.67 0.6], ...
                     'LineWidth', lw);
            end
        end
    end
    for c = 1:3
        m = com == c;
        scatter(pos(m, 1), pos(m, 2), 120, palette('cat', c), 'filled', ...
                'MarkerEdgeColor', 'w', 'LineWidth', 1.2, ...
                'DisplayName', sprintf('community %d', c));
    end
    legend('Location', 'southeast', 'FontSize', 8);
    title('Undirected network (communities)');
end
