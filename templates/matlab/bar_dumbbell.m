function fig = bar_dumbbell()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 8; labels = arrayfun(@(i)sprintf('item %d',i),1:n,'UniformOutput',false);
    before = 20 + 60*rand(1,n); after = before + 5 + 8*randn(1,n);
    y = 1:n;
    fig = figure; hold on;
    for i = 1:n
        plot([before(i) after(i)], [y(i) y(i)], 'Color', [0.75 0.75 0.75], 'LineWidth', 2);
    end
    plot(before, y, 'o', 'Color', palette('cat',1), 'MarkerFaceColor', palette('cat',1), 'MarkerSize', 8);
    plot(after,  y, 'o', 'Color', palette('cat',2), 'MarkerFaceColor', palette('cat',2), 'MarkerSize', 8);
    set(gca,'YTick',y,'YTickLabel',labels);
    xlabel('value'); title('Dumbbell');
    legend({'','before','after'}); grid on;
end
