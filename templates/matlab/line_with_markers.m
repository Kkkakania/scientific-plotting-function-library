function fig = line_with_markers()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    x = 1:12; markers = {'o','s','^','d'};
    fig = figure; hold on;
    for i = 1:4
        y = cumsum(randn(1, 12));
        plot(x, y, ['-' markers{i}], 'Color', palette('cat',i), ...
             'MarkerFaceColor','w', 'MarkerEdgeColor', palette('cat',i), ...
             'MarkerSize', 7, 'LineWidth', 1.5);
    end
    xlabel('month'); ylabel('value'); title('Line with markers');
    legend(arrayfun(@(i)sprintf('series %d',i),1:4,'UniformOutput',false));
    grid on;
end
