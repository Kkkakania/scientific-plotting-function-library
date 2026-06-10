function fig = heatmap_clustered()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    M = 0.3*randn(20, 15);
    for k = 1:floor(min(size(M))/2)
        M(k*2-1:k*2, k*2-1:k*2) = M(k*2-1:k*2, k*2-1:k*2) + 1;
    end
    Dr = pdist(M);   Lr = linkage(Dr, 'ward'); ro = optimalleaforder(Lr, Dr);
    Dc = pdist(M');  Lc = linkage(Dc, 'ward'); co = optimalleaforder(Lc, Dc);
    fig = figure; imagesc(M(ro, co));
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'value';
    title('Clustered heatmap'); set(gca,'XTick',[],'YTick',[]); axis tight;
end
