function fig = meta_funnel()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(13);
    pooled = 0.40; n_study = 30;
    se = 0.04 + 0.38*rand(1, n_study);
    eff = pooled + se.*randn(1, n_study);
    % small studies carry a positive bias -> mild asymmetry
    bias = se > 0.3;
    eff(bias) = eff(bias) + 0.25*se(bias);
    se_grid = linspace(0, 0.45, 100);
    gray = [0.5 0.5 0.5];
    fig = figure('Position', [100 100 560 440]); hold on;
    fill([pooled - 1.96*se_grid, fliplr(pooled + 1.96*se_grid)], ...
         [se_grid fliplr(se_grid)], palette('cat',1), ...
         'FaceAlpha', 0.08, 'EdgeColor', 'none');
    h95 = plot(pooled - 1.96*se_grid, se_grid, '--', 'Color', gray, 'LineWidth', 0.9);
    plot(pooled + 1.96*se_grid, se_grid, '--', 'Color', gray, 'LineWidth', 0.9);
    h99 = plot(pooled - 2.576*se_grid, se_grid, ':', 'Color', gray, 'LineWidth', 0.9);
    plot(pooled + 2.576*se_grid, se_grid, ':', 'Color', gray, 'LineWidth', 0.9);
    hst = scatter(eff, se, 30, palette('cat',1), 'filled', ...
                  'MarkerFaceAlpha', 0.75, 'MarkerEdgeColor', 'w', 'LineWidth', 0.4);
    hpl = plot([pooled pooled], [0 0.45], 'Color', palette('cat',2), 'LineWidth', 1.2);
    set(gca, 'YDir', 'reverse');              % SE axis inverted
    ylim([0 0.45]);
    xlabel('effect size (standardized mean difference)');
    ylabel('standard error');
    title('Funnel plot');
    legend([h95 h99 hst hpl], ...
           {'95% pseudo-CI', '99% pseudo-CI', 'studies', ...
            sprintf('pooled effect = %.2f', pooled)}, 'Location', 'southwest');
    grid on;
end
