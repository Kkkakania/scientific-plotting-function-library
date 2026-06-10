function fig = calendar_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    v = rand(1, 365);
    v(mod(0:364, 7) >= 5) = v(mod(0:364, 7) >= 5) * 0.4;
    M = nan(7, 53);
    for i = 1:365
        wk = floor((i-1)/7) + 1;
        wd = mod(i-1, 7) + 1;
        if wk <= 53, M(wd, wk) = v(i); end
    end
    fig = figure('Position',[100 100 900 300]);
    imagesc(M, 'AlphaData', ~isnan(M));
    colormap(palette('seq_green')); cb = colorbar; cb.Label.String = 'value';
    set(gca,'YTick',1:7,'YTickLabel',{'Mon','Tue','Wed','Thu','Fri','Sat','Sun'});
    xlabel('week'); title('Calendar heatmap'); axis tight;
end
