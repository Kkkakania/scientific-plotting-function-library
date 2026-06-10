function fig = raincloud()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    groups = {randn(200,1)*0.8, randn(200,1)*0.8 + 1.5, randn(200,1)*0.8 + 2.5};
    fig = figure('Position',[100 100 700 500]); hold on;
    for i = 1:numel(groups)
        arr = groups{i};
        [f, ys] = ksdensity(arr);
        f = f / max(f) * 0.35;
        fill([i*ones(size(ys)) fliplr(i + f)], [ys fliplr(ys)], palette('cat',i), ...
             'FaceAlpha', 0.6, 'EdgeColor', 'none');
        jitter = -0.15 + 0.13*rand(size(arr));
        scatter(i + jitter, arr, 8, palette('cat',i), 'filled', 'MarkerFaceAlpha', 0.5);
        qs = quantile(arr, [0.25 0.5 0.75]);
        plot([i-0.2 i-0.2], [qs(1) qs(3)], 'k', 'LineWidth', 4);
        scatter(i-0.2, qs(2), 20, 'w', 'filled');
    end
    set(gca,'XTick',1:3,'XTickLabel',{'A','B','C'});
    ylabel('value'); title('Raincloud plot'); grid on;
end
