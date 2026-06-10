function fig = violin_with_box()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    arrays = {randn(200,1), randn(200,1)+1, randn(200,1)+1.5, randn(200,1)+0.5};
    fig = figure; hold on;
    for i = 1:numel(arrays)
        [f, xi] = ksdensity(arrays{i});
        f = f / max(f) * 0.4;
        fill([i+f, i-fliplr(f)], [xi, fliplr(xi)], palette('cat',i), ...
             'FaceAlpha', 0.5, 'EdgeColor', palette('cat',i));
    end
    Y = nan(max(cellfun(@numel,arrays)), numel(arrays));
    for i=1:numel(arrays), Y(1:numel(arrays{i}),i) = arrays{i}; end
    boxplot(Y, 'Positions', 1:numel(arrays), 'Widths', 0.15, 'Symbol','');
    set(gca,'XTick',1:numel(arrays),'XTickLabel',{'A','B','C','D'});
    ylabel('value'); title('Violin + box'); grid on;
end
