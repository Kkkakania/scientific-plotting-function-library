function fig = heatmap_annotated()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    M = rand(6, 8);
    fig = figure; imagesc(M);
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'value';
    [r, c] = size(M); mu = mean(M(:));
    for i = 1:r
        for j = 1:c
            if M(i,j) > mu, col = 'w'; else, col = 'k'; end
            text(j, i, sprintf('%.2f', M(i,j)), 'Color', col, ...
                 'HorizontalAlignment','center', 'FontSize', 7);
        end
    end
    title('Annotated heatmap'); axis tight;
end
