function fig = bar_lollipop()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3); c = palette('cat',1);
    labels = arrayfun(@(i)sprintf('item %d',i),1:10,'UniformOutput',false);
    v = 20 + 70*rand(1, 10); [v, idx] = sort(v); labels = labels(idx);
    y = 1:numel(v);
    fig = figure; hold on;
    for i = 1:numel(v)
        plot([0 v(i)], [y(i) y(i)], 'Color', c, 'LineWidth', 1.5);
    end
    plot(v, y, 'o', 'Color', c, 'MarkerFaceColor', c, 'MarkerSize', 8);
    set(gca,'YTick',y,'YTickLabel',labels);
    xlabel('value'); title('Lollipop'); grid on;
end
