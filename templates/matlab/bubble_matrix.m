function fig = bubble_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    M = rand(8);
    [r, c] = size(M);
    [Y, X] = ndgrid(1:r, 1:c);
    fig = figure;
    scatter(X(:), Y(:), 600*(M(:)/max(M(:))), M(:), 'filled', ...
            'MarkerEdgeColor','w', 'LineWidth', 0.5);
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'value';
    set(gca,'YDir','reverse','XTick',1:c,'YTick',1:r);
    title('Bubble matrix'); xlim([0.5 c+0.5]); ylim([0.5 r+0.5]);
end
