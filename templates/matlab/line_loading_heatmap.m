function fig = line_loading_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    hours = 0:23; n_line = 10;
    base = 40 + 28*exp(-((hours - 11)/3.2).^2) + 22*exp(-((hours - 19)/2.2).^2);
    load_mat = max(min(base .* (0.55 + 0.7*rand(n_line, 1)) + 4*randn(n_line, 24), 130), 5);
    fig = figure;
    imagesc(hours, 1:n_line, load_mat); hold on;
    [yy, xx] = find(load_mat > 100);
    scatter(hours(xx), yy, 30, 'k', 'x', 'LineWidth', 1.1);
    colormap(sci_palettes('warm_lava'));
    cb = colorbar; cb.Label.String = 'loading (%)'; caxis([0 130]);
    yticks(1:n_line); yticklabels(arrayfun(@(i) sprintf('L%d', i), 1:n_line, 'UniformOutput', false));
    xlabel('hour'); ylabel('line'); title('Transmission line loading (% of rating)');
end
