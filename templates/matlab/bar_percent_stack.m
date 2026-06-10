function fig = bar_percent_stack()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    V = 10 + 40*rand(4, 5);
    Vp = V ./ sum(V, 1) * 100;
    fig = figure; b = bar(Vp', 'stacked');
    for k = 1:numel(b), b(k).FaceColor = palette('cat', k); end
    set(gca,'XTickLabel',arrayfun(@(i)sprintf('group %d',i),1:5,'UniformOutput',false));
    ylim([0 100]); ylabel('percentage (%)'); title('100% stacked bar');
    legend(arrayfun(@(i)sprintf('comp %d',i),1:4,'UniformOutput',false));
    grid on;
end
