function fig = dist_normal_family()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(-6, 6, 400);
    params = [0 0.5; 0 1; 0 2; -1 1; 2 0.8];
    fig = figure; hold on;
    for i = 1:size(params, 1)
        mu = params(i, 1); sigma = params(i, 2);
        pdf = exp(-(x-mu).^2 / (2*sigma^2)) / (sigma*sqrt(2*pi));
        plot(x, pdf, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('PDF'); title('Normal distribution family');
    legend(arrayfun(@(i)sprintf('\\mu=%g, \\sigma=%g', params(i,1), params(i,2)), ...
           1:size(params,1), 'UniformOutput', false));
    grid on;
end
