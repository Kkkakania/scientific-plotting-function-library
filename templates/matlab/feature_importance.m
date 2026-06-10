function fig = feature_importance()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    names = arrayfun(@(i)sprintf('feat_%d',i), 1:15, 'UniformOutput', false);
    imp = sort(exprnd(1, 15, 1), 'descend');
    cmap = palette('seq_blue');
    fig = figure;
    for i = 1:15
        c = cmap(round(50 + 200*imp(i)/max(imp)), :);
        barh(15-i+1, imp(i), 'FaceColor', c, 'EdgeColor','none'); hold on;
    end
    set(gca,'YTick',1:15,'YTickLabel',fliplr(names));
    xlabel('importance'); title('Feature importance'); grid on;
end
