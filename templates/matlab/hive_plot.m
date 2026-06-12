function fig = hive_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    n_per = 6;
    ang = deg2rad([90 210 330]);
    r0 = 0.55; r1 = 3.0;
    radii = linspace(0.95, 2.85, n_per);
    fig = figure('Position', [100 100 560 540]); hold on;
    tt = linspace(0, 1, 50)';
    pairs = [1 2; 2 3; 3 1];
    for p = 1:3                               % bezier links between axes
        a = pairs(p, 1); b = pairs(p, 2);
        c = palette('cat', p);
        cl = 1 - 0.5*(1 - c);                 % 50% faded link colour
        for e = 1:8
            ka = randi(n_per); kb = randi(n_per);
            p0 = radii(ka) * [cos(ang(a)) sin(ang(a))];
            p1 = radii(kb) * [cos(ang(b)) sin(ang(b))];
            mid = angle(exp(1i*ang(a)) + exp(1i*ang(b)));
            rm = 0.55 * (radii(ka) + radii(kb)) / 2;
            pc = rm * [cos(mid) sin(mid)];
            bez = (1 - tt).^2 * p0 + 2*tt.*(1 - tt) * pc + tt.^2 * p1;
            plot(bez(:, 1), bez(:, 2), 'Color', cl, 'LineWidth', 1.1);
        end
    end
    for a = 1:3                               % axes + nodes + class labels
        plot([r0 r1]*cos(ang(a)), [r0 r1]*sin(ang(a)), ...
             'Color', [0.478 0.510 0.541], 'LineWidth', 2.5);
        xs = radii*cos(ang(a)); ys = radii*sin(ang(a));
        scatter(xs, ys, 55, palette('cat', a), 'filled', ...
                'MarkerEdgeColor', 'w', 'LineWidth', 0.7);
        text(3.45*cos(ang(a)), 3.45*sin(ang(a)), sprintf('Type %c', char(64 + a)), ...
             'HorizontalAlignment', 'center', 'FontSize', 9);
    end
    axis equal; axis off;
    xlim([-3.7 3.7]); ylim([-3.2 3.9]);
    title('Hive plot (three node classes)', 'FontSize', 11);
end
