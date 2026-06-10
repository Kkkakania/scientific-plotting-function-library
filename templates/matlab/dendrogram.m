function fig = dendrogram_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(14);
    X = randn(15, 6);
    Z = linkage(X, 'ward');
    fig = figure('Position',[100 100 700 400]);
    dendrogram(Z, 'ColorThreshold', 'default');
    ylabel('distance'); title('Hierarchical dendrogram'); grid on;
end
