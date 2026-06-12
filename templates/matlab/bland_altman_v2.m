function fig = bland_altman_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    n = 100;
    true_v = 30 + 90*rand(n, 1);
    m1 = true_v + 3.0*randn(n, 1);
    m2 = true_v + 1.5 + 3.0*randn(n, 1);
    mn = (m1 + m2)/2; dif = m1 - m2;
    md = mean(dif); sd = std(dif);
    loa_lo = md - 1.96*sd; loa_hi = md + 1.96*sd;
    se_md = sd/sqrt(n);                 % SE of mean bias
    se_loa = sd*sqrt(3.0/n);            % approx SE of limits of agreement
    c0 = palette('cat', 1); c1 = palette('cat', 2);
    fig = figure; hold on;
    xs = [min(mn), max(mn)];
    bands = [md, se_md; loa_lo, se_loa; loa_hi, se_loa];
    for i = 1:3
        c = bands(i, 1); se = bands(i, 2);
        fill([xs(1) xs(2) xs(2) xs(1)], ...
             [c-1.96*se, c-1.96*se, c+1.96*se, c+1.96*se], c1, ...
             'FaceAlpha', 0.15, 'EdgeColor', 'none');
    end
    scatter(mn, dif, 28, c0, 'filled', 'MarkerFaceAlpha', 0.7, ...
            'MarkerEdgeColor', 'w', 'LineWidth', 0.4);
    h1 = yline(md, '-', 'Color', c1, 'LineWidth', 1.2);
    h2 = yline(loa_hi, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 1);
    h3 = yline(loa_lo, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 1);
    xlabel('mean of two methods'); ylabel('difference (method 1 - method 2)');
    title('Bland-Altman agreement');
    legend([h1 h2 h3], {sprintf('bias = %.2f', md), ...
           sprintf('+1.96 SD = %.2f', loa_hi), ...
           sprintf('-1.96 SD = %.2f', loa_lo)}, 'Location', 'northeast');
    grid on;
end
