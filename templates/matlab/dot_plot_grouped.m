function fig = dot_plot_grouped()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    labels = arrayfun(@(i)sprintf('item %d',i),1:8,'UniformOutput',false);
    V = 20 + 60*rand(3, 8);
    y = 1:8;
    fig = figure; hold on;
    for i = 1:3
        plot(V(i,:), y, 'o', 'Color', palette('cat',i), ...
             'MarkerFaceColor', palette('cat',i), 'MarkerSize', 8);
    end
    set(gca,'YTick',y,'YTickLabel',labels);
    xlabel('value'); title('Grouped dot plot');
    legend({'Q1','Q2','Q3'}); grid on;
end
