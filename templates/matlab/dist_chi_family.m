function fig = dist_chi_family()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0.01, 25, 400);
    dfs = [2 4 6 10 15];
    fig = figure; hold on;
    for i = 1:numel(dfs)
        plot(x, chi2pdf(x, dfs(i)), 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('PDF'); title('Chi-square family');
    legend(arrayfun(@(d)sprintf('df=%d',d), dfs, 'UniformOutput', false));
    grid on;
end
