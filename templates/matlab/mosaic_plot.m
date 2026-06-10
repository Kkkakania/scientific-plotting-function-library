function fig = mosaic_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    M = [40 20 10; 25 50 25; 15 30 45];
    rowS = sum(M, 2); total = sum(M(:));
    fig = figure('Position',[100 100 650 500]); hold on;
    y0 = 0;
    for i = 1:3
        h = rowS(i) / total; x0 = 0;
        for j = 1:3
            w = M(i, j) / rowS(i);
            rectangle('Position', [x0 y0 w h], 'FaceColor', palette('cat',j), 'EdgeColor','w');
            text(x0 + w/2, y0 + h/2, sprintf('%d', M(i, j)), ...
                 'HorizontalAlignment','center', 'Color','w');
            x0 = x0 + w;
        end
        y0 = y0 + h;
    end
    xlim([0 1]); ylim([0 1]);
    set(gca,'XTick',[],'YTick',[]);
    title('Mosaic plot');
end
