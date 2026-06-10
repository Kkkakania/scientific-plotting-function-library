function fig = density_hexbin()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    x = randn(10000,1); y = 0.7*x + 0.6*randn(10000,1);
    fig = figure;
    histogram2(x, y, 30, 'DisplayStyle','tile', 'EdgeColor','none');
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'count';
    xlabel('x'); ylabel('y'); title('Hexbin-like 2D histogram');
end
