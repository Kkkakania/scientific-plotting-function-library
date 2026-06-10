function fig = ecdf_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    locs = [-1 0 1.5];
    fig = figure; hold on;
    for i = 1:3
        data = sort(randn(400,1) + locs(i));
        ys = (1:numel(data))' / numel(data);
        stairs(data, ys, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('value'); ylabel('P(X \leq x)'); title('ECDF');
    legend(arrayfun(@(l)sprintf('\\mu=%g',l),locs,'UniformOutput',false));
    grid on;
end
