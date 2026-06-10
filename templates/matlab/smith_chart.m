function fig = smith_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    theta = linspace(0, 2*pi, 360);
    fig = figure('Position',[100 100 650 650]);
    plot(cos(theta), sin(theta), 'k', 'LineWidth', 1); hold on;
    rs = [0.2 0.5 1.0 2.0 5.0];
    for k = 1:numel(rs)
        r = rs(k); cx = r/(r+1); R = 1/(r+1);
        plot(cx + R*cos(theta), R*sin(theta), 'Color', [0.55 0.55 0.55], 'LineWidth', 0.7);
        text(cx + R - 0.02, 0.02, sprintf('%g',r), 'FontSize', 7);
    end
    xs = [0.2 0.5 1 2 5 -0.2 -0.5 -1 -2 -5];
    for k = 1:numel(xs)
        x = xs(k); cx = 1; cy = 1/x; R = abs(1/x);
        cxs = cx + R*cos(theta); cys = cy + R*sin(theta);
        mask = cxs.^2 + cys.^2 <= 1 + 1e-9;
        plot(cxs(mask), cys(mask), 'Color', [0.75 0.75 0.75], 'LineWidth', 0.6);
    end
    plot([-1 1], [0 0], 'k', 'LineWidth', 0.8);
    axis equal off; xlim([-1.1 1.1]); ylim([-1.1 1.1]);
    title('Smith chart');
end
