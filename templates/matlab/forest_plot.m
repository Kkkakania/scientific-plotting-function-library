function fig = forest_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6); c = palette('cat',1);
    n = 8; labels = arrayfun(@(i)sprintf('study %d',i),1:n,'UniformOutput',false);
    effects = 0.5 + 0.4*randn(n,1); widths = 0.2 + 0.4*rand(n,1);
    lo = effects - widths; hi = effects + widths;
    y = fliplr(1:n);
    fig = figure; hold on;
    for i = 1:n
        plot([lo(i) hi(i)], [y(i) y(i)], 'Color', [0.55 0.55 0.55], 'LineWidth', 1.2);
    end
    plot(effects, y, 's', 'Color', c, 'MarkerFaceColor', c, 'MarkerSize', 9);
    xline(0, 'k');
    set(gca,'YTick',sort(y),'YTickLabel',fliplr(labels));
    xlabel('effect size'); title('Forest plot'); grid on;
end
