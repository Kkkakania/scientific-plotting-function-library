function fig = scree_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    eigvals = sort(exprnd(2, 10, 1) + linspace(8, 0.1, 10)', 'descend');
    cum = cumsum(eigvals) / sum(eigvals) * 100;
    fig = figure;
    yyaxis left;
    bar(1:10, eigvals, 'FaceColor', palette('cat',1)); ylabel('eigenvalue');
    yyaxis right;
    plot(1:10, cum, '-o', 'Color', palette('cat',2), 'LineWidth', 1.5);
    yline(80, '--', 'Color', [0.5 0.5 0.5]);
    ylabel('cumulative (%)');
    xlabel('component'); title('Scree plot'); grid on;
end
