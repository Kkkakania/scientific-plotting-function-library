function fig = wind_rose()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    n_dir = 16; bins = {'0-3', '3-6', '6-9', '9-12', '>12 m/s'};
    k = 0:n_dir-1;
    prevail = exp(-0.5*(mod(k - 4, n_dir)/2.5).^2) + 0.6*exp(-0.5*(mod(k - 12, n_dir)/2.0).^2);
    freq = prevail' * [0.30 0.30 0.22 0.12 0.06];
    freq = freq .* (1 + 0.3*(rand(size(freq)) - 0.5));
    freq = freq/sum(freq(:))*100;
    theta = k*2*pi/n_dir;            % 0 = 北，顺时针
    half = pi/n_dir*0.9;
    cmap = sci_palettes('blues', 8);
    fig = figure; hold on; axis equal off;
    hs = gobjects(1, numel(bins));
    for j = 1:numel(bins)
        for d = 1:n_dir
            r0 = sum(freq(d, 1:j-1)); r1 = r0 + freq(d, j);
            tt = linspace(theta(d) - half, theta(d) + half, 12);
            x = [r0*sin(tt) fliplr(r1*sin(tt))];
            y = [r0*cos(tt) fliplr(r1*cos(tt))];
            h = fill(x, y, cmap(2+j, :), 'EdgeColor', 'w', 'LineWidth', 0.3);
            if d == 1, hs(j) = h; end
        end
    end
    rmax = max(sum(freq, 2));
    for r = linspace(rmax/3, rmax, 3)
        tt = linspace(0, 2*pi, 120);
        plot(r*sin(tt), r*cos(tt), ':', 'Color', [0.7 0.7 0.7], 'LineWidth', 0.6);
        text(r*sin(pi/8), r*cos(pi/8), sprintf('%.1f%%', r), 'FontSize', 7, 'Color', [0.45 0.45 0.45]);
    end
    dirs = {'N','NE','E','SE','S','SW','W','NW'};
    for i = 1:8
        a = (i-1)*pi/4;
        text(1.12*rmax*sin(a), 1.12*rmax*cos(a), dirs{i}, 'HorizontalAlignment', 'center');
    end
    legend(hs, bins, 'Location', 'southeastoutside', 'FontSize', 7);
    title('Wind rose');
end
