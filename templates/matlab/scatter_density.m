function fig = scatter_density()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    x = randn(2000,1); y = 0.6*x + 0.8*randn(2000,1);
    [N, ce] = hist3([x y], 'Nbins', [40 40]);
    [~, ix] = histc(x, ce{1}); [~, iy] = histc(y, ce{2});
    ix = max(min(ix, 40), 1); iy = max(min(iy, 40), 1);
    z = arrayfun(@(i,j) N(i,j), ix, iy);
    [~, idx] = sort(z);
    fig = figure;
    scatter(x(idx), y(idx), 8, z(idx), 'filled');
    colormap(hot); cb = colorbar; cb.Label.String = 'density';
    xlabel('x'); ylabel('y'); title('Density scatter');
end
