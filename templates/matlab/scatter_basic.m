function fig = scatter_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    x = randn(150, 1); y = randn(150, 1);
    fig = figure;
    scatter(x, y, 30, palette('cat',1), 'filled', 'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w');
    xlabel('x'); ylabel('y'); title('Scatter'); grid on;
end
