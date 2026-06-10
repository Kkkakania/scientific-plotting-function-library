function fig = bar_diverging()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    labels = arrayfun(@(i)sprintf('factor %d',i),1:10,'UniformOutput',false);
    v = -5 + 10*rand(1, 10); [v, idx] = sort(v); labels = labels(idx);
    fig = figure; hold on;
    for i = 1:numel(v)
        if v(i) < 0, c = palette('cat',2); else, c = palette('cat',1); end
        barh(i, v(i), 'FaceColor', c, 'EdgeColor','none');
    end
    set(gca,'YTick',1:numel(v),'YTickLabel',labels);
    xline(0, 'k'); xlabel('effect'); title('Diverging bar'); grid on;
end
