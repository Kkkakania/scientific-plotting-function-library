function fig = fan_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(17);
    t_hist = 0:30;
    y_hist = 50 + 0.6*t_hist + 3*sin(t_hist/3) + 1.2*randn(1, 31);
    h = 0:20;
    t_fc = 30 + h;
    center = y_hist(end) + 0.55*h;
    sigma = 1.5*sqrt(max(h, 1e-9));
    qs = [0.05 0.10 0.20 0.35];               % paired quantile bands
    fig = figure; hold on;
    hb = gobjects(1, numel(qs));
    for i = 1:numel(qs)
        z = sqrt(2)*erfinv(2*(1 - qs(i)) - 1);    % normal quantile, base MATLAB
        hb(i) = fill([t_fc fliplr(t_fc)], ...
                     [center - z*sigma, fliplr(center + z*sigma)], ...
                     palette('cat',1), 'FaceAlpha', 0.13 + 0.07*(i-1), ...
                     'EdgeColor', 'none');
    end
    hobs = plot(t_hist, y_hist, 'k-', 'LineWidth', 1.2);
    hmed = plot(t_fc, center, '--', 'Color', palette('cat',2), 'LineWidth', 1.3);
    yl = ylim;
    plot([30 30], yl, ':', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.9);
    text(30.4, yl(1) + 1, 'forecast start', 'FontSize', 7, 'Color', [0.5 0.5 0.5], ...
         'Rotation', 90, 'VerticalAlignment', 'bottom');
    ylim(yl);
    xlabel('time'); ylabel('value'); title('Fan chart forecast');
    legend([hb(1) hb(end) hobs hmed], ...
           {'90% band', '30% band', 'observed', 'median forecast'}, ...
           'Location', 'northwest');
    grid on;
end
