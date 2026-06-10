function fig = funnel_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    stages = {'visit','sign-up','add to cart','checkout','paid'};
    values = [10000 4800 2100 1200 850];
    cmap = palette('seq_blue');
    fig = figure('Position',[100 100 650 500]); hold on;
    max_v = max(values);
    for i = 1:numel(stages)
        w = values(i) / max_v; y = numel(stages) - i;
        c = cmap(round(80 + 175*values(i)/max_v), :);
        rectangle('Position',[-w, y, 2*w, 0.8], 'FaceColor', c, 'EdgeColor','w');
        text(0, y+0.4, sprintf('%s: %d', stages{i}, values(i)), ...
             'HorizontalAlignment','center', 'Color','w', 'FontWeight','bold');
    end
    xlim([-1.1 1.1]); ylim([-0.5 numel(stages)+0.2]);
    set(gca,'XTick',[],'YTick',[]); box off;
    title('Funnel chart');
end
