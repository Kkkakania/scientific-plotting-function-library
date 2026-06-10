function fig = dist_beta_family()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0.001, 0.999, 400);
    params = [0.5 0.5; 1 1; 2 5; 5 2; 8 8];
    fig = figure; hold on;
    for i = 1:size(params, 1)
        plot(x, betapdf(x, params(i, 1), params(i, 2)), ...
             'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('PDF'); title('Beta family');
    legend(arrayfun(@(i)sprintf('\\alpha=%g, \\beta=%g', params(i,1), params(i,2)), ...
           1:size(params,1), 'UniformOutput', false));
    grid on;
end
