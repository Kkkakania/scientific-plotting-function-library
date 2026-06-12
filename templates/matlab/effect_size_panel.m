function fig = effect_size_panel()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    mu1 = 0.0; mu2 = 1.2; sd = 1.0;
    d = (mu2 - mu1) / sd;
    x = linspace(min(mu1, mu2) - 4*sd, max(mu1, mu2) + 4*sd, 500);
    pdf1 = exp(-0.5*((x - mu1)/sd).^2) / (sd*sqrt(2*pi));
    pdf2 = exp(-0.5*((x - mu2)/sd).^2) / (sd*sqrt(2*pi));
    ov = min(pdf1, pdf2);
    fig = figure; hold on;
    hov = fill([x fliplr(x)], [ov zeros(size(ov))], [0.5 0.5 0.5], ...
               'FaceAlpha', 0.35, 'EdgeColor', 'none');
    h1 = plot(x, pdf1, 'Color', palette('cat',1), 'LineWidth', 1.5);
    h2 = plot(x, pdf2, 'Color', palette('cat',2), 'LineWidth', 1.5);
    ymax = max(pdf1);
    % double-headed arrow between the two means + Cohen's d label
    plot([mu1 mu2], [1 1]*ymax*1.06, 'k-', 'LineWidth', 1.1);
    plot(mu1, ymax*1.06, 'k<', 'MarkerFaceColor', 'k', 'MarkerSize', 4);
    plot(mu2, ymax*1.06, 'k>', 'MarkerFaceColor', 'k', 'MarkerSize', 4);
    text((mu1 + mu2)/2, ymax*1.10, sprintf('d = %.2f', d), ...
         'HorizontalAlignment', 'center', 'FontSize', 9);
    % benchmark ruler: small / medium / large
    bench = [0.2 0.5 0.8]; lbls = {'small', 'medium', 'large'};
    for i = 1:3
        xb = mu1 + bench(i)*sd;
        plot([xb xb], [ymax*1.00 ymax*1.03], 'Color', [0.5 0.5 0.5], 'LineWidth', 0.9);
        text(xb, ymax*0.965, lbls{i}, 'HorizontalAlignment', 'center', ...
             'FontSize', 7, 'Color', [0.5 0.5 0.5]);
    end
    plot([mu1 mu1], [0 ymax], ':', 'Color', palette('cat',1), 'LineWidth', 0.9);
    plot([mu2 mu2], [0 ymax], ':', 'Color', palette('cat',2), 'LineWidth', 0.9);
    ylim([0 ymax*1.22]);
    xlabel('outcome value'); ylabel('density'); title('Effect size: Cohen''s d');
    legend([h1 h2 hov], {'group 1', 'group 2', 'overlap'}, 'Location', 'northwest');
    grid on;
end
