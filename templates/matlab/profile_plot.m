function fig = profile_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    metrics = {'speed','cost','noise','efficiency','durability'};
    M = 2 + 7*rand(3, 5);
    fig = figure;
    hold on;
    for i = 1:3
        plot(1:5, M(i,:), '-o', 'Color', palette('cat',i), 'LineWidth', 1.5, 'MarkerSize', 7);
    end
    set(gca,'XTick',1:5,'XTickLabel',metrics);
    ylim([0 10]); ylabel('score'); title('Profile plot');
    legend({'A','B','C'}); grid on;
end
