function fig = histogram_cumulative()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    data = randn(1000, 1);
    fig = figure;
    histogram(data, 50, 'Normalization','cdf', 'DisplayStyle','stairs', ...
              'EdgeColor', palette('cat',1), 'LineWidth', 1.5);
    xlabel('value'); ylabel('cumulative P'); title('Cumulative histogram'); grid on;
end
