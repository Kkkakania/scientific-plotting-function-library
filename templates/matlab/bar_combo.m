function fig = bar_combo()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    months = arrayfun(@(i)sprintf('M%d',i),1:12,'UniformOutput',false);
    sales = 30 + 70*rand(1, 12);
    growth = gradient(sales)./sales*100;
    fig = figure;
    yyaxis left;  bar(sales, 'FaceColor', palette('cat',1)); ylabel('sales');
    set(gca,'XTick',1:12,'XTickLabel',months);
    yyaxis right; plot(1:12, growth, '-o', 'Color', palette('cat',2), 'LineWidth', 1.5);
    ylabel('growth (%)'); title('Bar + line combo'); grid on;
end
