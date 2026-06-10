function fig = heatmap_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    M = rand(8, 12);
    fig = figure; imagesc(M);
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'value';
    xlabel('column'); ylabel('row'); title('Heatmap'); axis tight;
end
