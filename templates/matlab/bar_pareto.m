function fig = bar_pareto()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    n = 8; counts = sort(5 + 55*rand(1, n), 'descend');
    cum = cumsum(counts)/sum(counts)*100;
    fig = figure;
    yyaxis left;  bar(counts, 'FaceColor', palette('cat',1)); ylabel('count');
    set(gca,'XTickLabel',arrayfun(@(i)sprintf('cause %d',i),1:n,'UniformOutput',false));
    yyaxis right; plot(1:n, cum, '-o', 'Color', palette('cat',2), 'LineWidth', 1.5);
    ylim([0 105]); ylabel('cumulative (%)'); yline(80, '--', 'Color', [0.5 0.5 0.5]);
    title('Pareto chart');
end
