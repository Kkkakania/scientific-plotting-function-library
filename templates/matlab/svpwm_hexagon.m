function fig = svpwm_hexagon()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    a = linspace(0, 2*pi, 7); vx = cos(a); vy = sin(a);
    fig = figure('Position',[100 100 600 600]);
    plot(vx, vy, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    scatter(vx(1:end-1), vy(1:end-1), 60, palette('cat',1), 'filled');
    for i = 1:6, text(vx(i)*1.12, vy(i)*1.12, sprintf('V%d',i), 'HorizontalAlignment','center'); end
    th = linspace(0, 2*pi, 100);
    plot(0.85*cos(th), 0.85*sin(th), '--', 'Color', [0.5 0.5 0.5]);
    quiver(0, 0, 0.85*cos(pi/6), 0.85*sin(pi/6), 0, 'Color', palette('cat',2), 'LineWidth', 2);
    xline(0,'Color',[0.6 0.6 0.6]); yline(0,'Color',[0.6 0.6 0.6]);
    axis equal; xlim([-1.3 1.3]); ylim([-1.3 1.3]);
    xlabel('\alpha'); ylabel('\beta'); title('SVPWM hexagon');
end
