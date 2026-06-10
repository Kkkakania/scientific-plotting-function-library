function fig = histogram_2d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    x = randn(5000,1); y = 0.6*x + 0.8*randn(5000,1);
    fig = figure;
    histogram2(x, y, 40, 'DisplayStyle','tile', 'EdgeColor','none');
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'count';
    xlabel('x'); ylabel('y'); title('2D histogram');
end
