function fig = joint_marginal()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3); c = palette('cat',1);
    x = randn(600,1); y = 0.6*x + 0.7*randn(600,1);
    fig = figure('Position',[100 100 600 600]);
    ax_main  = subplot(4, 4, [5 6 7 9 10 11 13 14 15]);
    scatter(ax_main, x, y, 10, c, 'filled', 'MarkerFaceAlpha', 0.6);
    xlabel(ax_main, 'x'); ylabel(ax_main, 'y');
    ax_top   = subplot(4, 4, [1 2 3]);
    histogram(ax_top, x, 30, 'FaceColor', c, 'EdgeColor','w'); set(ax_top,'XTick',[]);
    ax_right = subplot(4, 4, [8 12 16]);
    histogram(ax_right, y, 30, 'FaceColor', c, 'EdgeColor','w', 'Orientation','horizontal');
    set(ax_right,'YTick',[]);
    sgtitle('Joint + marginals');
end
