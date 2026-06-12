function fig = credible_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    names = {'intercept', 'slope_x1', 'slope_x2', 'slope_x3', ...
             'interaction', 'group_sd', 'noise_sd'};
    mus = [1.8 0.65 -0.42 0.08 -0.95 0.55 1.10];
    sds = [0.30 0.18 0.15 0.20 0.35 0.12 0.10];
    np = numel(mus);
    fig = figure('Position', [100 100 600 440]); hold on;
    ypos = np:-1:1;
    for k = 1:np
        t5 = randn(4000, 1)./sqrt(sum(randn(4000, 5).^2, 2)/5);  % Student-t(5)
        draws = mus(k) + sds(k)*randn(4000, 1) + 0.1*sds(k)*t5;
        [lo, hi] = hdi(draws, 0.94);
        med = median(draws);
        plot([lo hi], [ypos(k) ypos(k)], 'Color', palette('cat', 1), 'LineWidth', 2.2);
        plot(med, ypos(k), 'o', 'Color', palette('cat', 2), ...
             'MarkerFaceColor', palette('cat', 2), 'MarkerSize', 6);
    end
    xline(0, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.9);
    set(gca, 'YTick', 1:np, 'YTickLabel', fliplr(names), ...
        'TickLabelInterpreter', 'none');
    ylim([0.5, np+0.5]);
    xlabel('parameter value'); ylabel('parameter');
    title('Posterior medians with 94% HDI');
    ax = gca; ax.XGrid = 'on'; ax.YGrid = 'off';
end

function [lo, hi] = hdi(x, cred)
    xs = sort(x(:)); n = numel(xs);
    m = ceil(cred*n);
    widths = xs(m:end) - xs(1:n-m+1);
    [~, i] = min(widths);
    lo = xs(i); hi = xs(i+m-1);
end
