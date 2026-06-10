function fig = zoomed_inset()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat',1);
    t = linspace(0, 1, 2000); y = sin(2*pi*5*t) + 0.3*sin(2*pi*50*t);
    fig = figure('Position',[100 100 700 400]);
    ax1 = axes('Position',[0.1 0.12 0.85 0.78]);
    plot(ax1, t, y, 'Color', c, 'LineWidth', 1);
    xlabel('t'); ylabel('y'); title('Zoomed inset'); grid on;
    ax2 = axes('Position',[0.58 0.55 0.32 0.30]);
    plot(ax2, t, y, 'Color', c, 'LineWidth', 1);
    xlim(ax2, [0.40 0.46]); ylim(ax2, [-1.5 1.5]);
    set(ax2,'XTick',[],'YTick',[]); box(ax2,'on');
end
