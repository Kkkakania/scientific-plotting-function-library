function fig = silhouette_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    centers = [0 0; 4 4; -3 4];
    n = 50;
    X = [randn(n,2)+centers(1,:); randn(n,2)+centers(2,:); randn(n,2)+centers(3,:)] * 0.9;
    labels = [ones(n,1); 2*ones(n,1); 3*ones(n,1)];
    fig = figure('Position',[100 100 600 500]);
    silhouette(X, labels);
    title('Silhouette plot'); grid on;
end
