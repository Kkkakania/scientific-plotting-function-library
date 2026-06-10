function fig = paired_slope()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    before = 20 + 60*rand(25,1); after = before + 5 + 8*randn(25,1);
    fig = figure; hold on;
    for i = 1:25
        if after(i) > before(i), c = palette('cat',1); else, c = palette('cat',2); end
        plot([0 1], [before(i) after(i)], '-o', 'Color', c, 'MarkerFaceColor', c, ...
             'MarkerSize', 4, 'LineWidth', 1);
    end
    set(gca,'XTick',[0 1],'XTickLabel',{'before','after'});
    xlim([-0.3 1.3]); ylabel('measurement'); title('Paired slope'); grid on;
end
