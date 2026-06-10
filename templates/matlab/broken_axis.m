function fig = broken_axis()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat',1);
    x = 0:9; y = [linspace(1,15,8) 95 100];
    fig = figure('Position',[100 100 600 400]);
    ax1 = subplot(4, 1, 1);    bar(x, y, 'FaceColor', c); ylim([90 105]);
    ax2 = subplot(4, 1, 2:4);  bar(x, y, 'FaceColor', c); ylim([0 20]);
    ax1.XAxis.Visible = 'off'; ax1.YTick = [95 100];
    title(ax1, 'Broken axis'); xlabel(ax2, 'category'); ylabel(ax2, 'value');
end
