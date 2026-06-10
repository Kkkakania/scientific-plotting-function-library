function fig = heatmap_dendro()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    M = 0.3*randn(20, 15);
    for k = 1:floor(min(size(M))/2)
        M(k*2-1:k*2, k*2-1:k*2) = M(k*2-1:k*2, k*2-1:k*2) + 1;
    end
    Zr = linkage(M,   'ward'); ro = optimalleaforder(Zr, pdist(M));
    Zc = linkage(M.', 'ward'); co = optimalleaforder(Zc, pdist(M.'));
    fig = figure('Position',[100 100 700 600]);
    ax_top = subplot('Position',[0.25 0.78 0.65 0.18]);
    dendrogram(Zc, 0, 'Reorder', co); axis off;
    ax_left = subplot('Position',[0.06 0.08 0.18 0.65]);
    dendrogram(Zr, 0, 'Orientation','left', 'Reorder', ro); axis off;
    ax_main = subplot('Position',[0.25 0.08 0.65 0.65]);
    imagesc(M(ro, co)); colormap(palette('div'));
    set(ax_main,'XTick',[],'YTick',[]); colorbar('east');
    sgtitle('Heatmap + dendrogram');
end
