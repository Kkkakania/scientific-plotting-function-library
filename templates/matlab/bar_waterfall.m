function fig = bar_waterfall()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    labels = {'start','A','B','C','D','end'};
    v = [50 15 -8 22 -10 0];
    v(end) = sum(v(1:end-1));
    cum = [0 cumsum(v(1:end-1))];
    fig = figure; hold on;
    for i = 1:numel(v)
        if i == 1 || i == numel(v)
            bar(i, v(i), 'FaceColor', palette('cat',8));
        elseif v(i) > 0
            bar(i, v(i), 'BaseValue', cum(i), 'FaceColor', palette('cat',1));
        else
            bar(i, v(i), 'BaseValue', cum(i), 'FaceColor', palette('cat',2));
        end
    end
    set(gca,'XTick',1:numel(v),'XTickLabel',labels);
    ylabel('value'); title('Waterfall'); grid on;
end
