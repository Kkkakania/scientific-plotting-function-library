function fig = double_triangle_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    A = rand(10); B = 2*rand(10) - 1;
    up = A .* triu(ones(10), 1); up(up == 0) = NaN;
    lo = B .* tril(ones(10), -1); lo(lo == 0) = NaN;
    fig = figure;
    h1 = imagesc(up); set(h1, 'AlphaData', ~isnan(up)); hold on;
    colormap(palette('seq_blue')); freezeColors_local;
    h2 = imagesc(lo); set(h2, 'AlphaData', ~isnan(lo));
    colormap(palette('div'));
    title('Double-triangle heatmap'); axis tight; set(gca,'XTick',[],'YTick',[]);
end

function freezeColors_local()
    % no-op placeholder; if using multiple colormaps, consider colormap subplots
end
