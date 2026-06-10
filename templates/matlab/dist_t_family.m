function fig = dist_t_family()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(-5, 5, 400);
    dfs = [1 2 5 30];
    fig = figure; hold on;
    for i = 1:numel(dfs)
        plot(x, tpdf(x, dfs(i)), 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    plot(x, normpdf(x), '--k', 'LineWidth', 0.8);
    xlabel('x'); ylabel('PDF'); title("Student's t family");
    legend([arrayfun(@(d)sprintf('df=%d',d), dfs, 'UniformOutput', false), {'N(0,1)'}]);
    grid on;
end
