function fig = anomaly_timeline()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(13);
    n = 300; t = 0:n-1;
    y = 10 + 2*sin(2*pi*t/50) + 0.4*randn(1, n);
    spans = [80 95; 160 172; 238 252];
    y(81:95)   = y(81:95) + 3.0;
    y(161:172) = y(161:172) + 2.0*randn(1, 12);
    y(239:252) = y(239:252) - linspace(0, 4, 14);
    mask = false(1, n);
    for s = 1:size(spans, 1), mask(spans(s,1)+1:spans(s,2)) = true; end
    c0 = palette('cat', 1); c1 = palette('cat', 2);
    fig = figure('Position', [100 100 800 400]); hold on;
    yl = [min(y)-0.6, max(y)+0.9];
    hw = gobjects(1, size(spans, 1));
    for s = 1:size(spans, 1)
        a = spans(s, 1); b = spans(s, 2);
        hw(s) = fill([a b b a], [yl(1) yl(1) yl(2) yl(2)], c1, ...
                     'FaceAlpha', 0.15, 'EdgeColor', 'none');
        text((a+b)/2, yl(2), sprintf('E%d', s), 'HorizontalAlignment', 'center', ...
             'VerticalAlignment', 'bottom', 'FontSize', 8, 'Color', c1);
    end
    hs = plot(t, y, 'Color', c0, 'LineWidth', 1.1);
    hf = plot(t(mask), y(mask), '.', 'Color', c1, 'MarkerSize', 8);
    xlim([0 n-1]); ylim([yl(1), yl(2)+0.8]);
    xlabel('time (sample)'); ylabel('sensor reading'); title('Anomaly timeline');
    legend([hw(1) hs hf], {'anomaly window', 'signal', 'flagged points'}, ...
           'Location', 'southwest', 'FontSize', 7);
    grid on;
end
