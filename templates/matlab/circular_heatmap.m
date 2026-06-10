function fig = circular_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(16);
    n_t = 24; n_r = 6;
    M = rand(n_r, n_t);
    theta = linspace(0, 2*pi, n_t+1);
    r = linspace(0.3, 1.0, n_r+1);
    fig = figure('Position',[100 100 600 600]);
    pax = polaraxes; hold(pax, 'on');
    for i = 1:n_r
        for j = 1:n_t
            t1 = theta(j); t2 = theta(j+1);
            r1 = r(i);    r2 = r(i+1);
            tt = linspace(t1, t2, 10);
            xx = [r1*cos(tt) r2*cos(fliplr(tt))];
            yy = [r1*sin(tt) r2*sin(fliplr(tt))];
            [th, rr] = cart2pol(xx, yy);
            polarscatter(pax, th, rr, 1, 'w'); % placeholder so axes exist
            patch(pax, 'XData', xx, 'YData', yy, 'CData', M(i,j), ...
                  'FaceColor','flat', 'EdgeColor','none');
        end
    end
    colormap(palette('seq_orange')); colorbar;
    title('Circular heatmap');
end
