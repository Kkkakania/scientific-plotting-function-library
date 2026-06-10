function fig = heatmap_categorical()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    M = randi([1 5], 8, 12);
    pal = zeros(5, 3);
    for k = 1:5, pal(k, :) = palette('cat', k); end
    fig = figure;
    imagesc(M, [0.5 5.5]);
    colormap(pal); cb = colorbar; cb.Ticks = 1:5;
    cb.TickLabels = arrayfun(@(i)sprintf('cat %d',i), 1:5, 'UniformOutput', false);
    xlabel('column'); ylabel('row'); title('Categorical heatmap');
end
