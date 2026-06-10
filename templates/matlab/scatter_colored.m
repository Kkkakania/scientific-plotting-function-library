function fig = scatter_colored()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    x = randn(200,1); y = randn(200,1); c = x.^2 + y.^2;
    fig = figure;
    scatter(x, y, 30, c, 'filled', 'MarkerFaceAlpha', 0.85, 'MarkerEdgeColor','w');
    colormap(parula); cb = colorbar; cb.Label.String = 'value';
    xlabel('x'); ylabel('y'); title('Color-coded scatter'); grid on;
end
