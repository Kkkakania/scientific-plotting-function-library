function fig = shap_summary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(9);
    n_feat = 8; n = 200;
    shap = randn(n_feat, n);
    [~, idx] = sort(mean(abs(shap), 2), 'descend');
    shap = shap(idx, :);
    fval = rand(n_feat, n);
    fig = figure('Position',[100 100 700 500]); hold on;
    for i = 1:n_feat
        y = i + 0.3*(2*rand(1, n) - 1);
        scatter(shap(i, :), y, 15, fval(i, :), 'filled', 'MarkerFaceAlpha', 0.8);
    end
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'feature value';
    xline(0, 'Color', [0.5 0.5 0.5]);
    set(gca,'YTick',1:n_feat,'YTickLabel', ...
        arrayfun(@(i)sprintf('feat_%d',i),1:n_feat,'UniformOutput',false), 'YDir', 'reverse');
    xlabel('SHAP value'); title('SHAP summary');
end
