function fig = step_after_compare()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(19);
    sw = 50; n = 100;
    t = 0:n-1;
    y = 5.0 * (t < sw) + 6.5 * (t >= sw) + 0.6 * randn(1, n);
    fig = figure; hold on;
    hobs = plot(t, y, '.', 'Color', [0.6 0.6 0.6], 'MarkerSize', 8);
    masks = {t < sw, t >= sw};
    names = {'before', 'after'};
    hseg = gobjects(1, 2); labels = cell(1, 2);
    for k = 1:2
        mask = masks{k}; c = palette('cat',k);
        m = mean(y(mask)); s = std(y(mask));
        ci = 1.96 * s / sqrt(sum(mask));
        tt = t(mask);
        fill([tt(1) tt(end) tt(end) tt(1)], [m-ci m-ci m+ci m+ci], c, ...
             'FaceAlpha', 0.2, 'EdgeColor', 'none');
        hseg(k) = plot([tt(1) tt(end)], [m m], 'Color', c, 'LineWidth', 2.2);
        labels{k} = sprintf('%s mean = %.2f', names{k}, m);
    end
    yl = ylim;
    plot([sw-0.5 sw-0.5], yl, '--', 'Color', [0.4 0.4 0.4], 'LineWidth', 1);
    text(sw - 0.5, yl(2), ' intervention', 'FontSize', 8, ...
         'VerticalAlignment', 'top', 'Color', [0.4 0.4 0.4]);
    ylim(yl);
    xlabel('time (sample)'); ylabel('process output');
    title('Before / after step comparison');
    legend([hobs hseg], [{'observations'} labels], ...
           'Location', 'southeast', 'FontSize', 8, 'Box', 'off');
    grid on;
end
