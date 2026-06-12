function fig = chord_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    n = 6;
    F = double(randi([0 8], n, n));
    F(F < 3) = 0;
    F(1:n+1:end) = 0;
    totals = sum(F, 1)' + sum(F, 2);
    gap = 0.05;
    span = (2*pi - n*gap)*totals/sum(totals);
    starts = pi/2 + [0; cumsum(span(1:end-1) + gap)];
    seg_o = zeros(n, n, 2); seg_i = zeros(n, n, 2);
    cur = starts;
    for i = 1:n
        for j = 1:n
            if F(i, j) > 0
                w = F(i, j)/totals(i)*span(i);
                seg_o(i, j, :) = [cur(i), cur(i)+w]; cur(i) = cur(i) + w;
            end
        end
        for j = 1:n
            if F(j, i) > 0
                w = F(j, i)/totals(i)*span(i);
                seg_i(i, j, :) = [cur(i), cur(i)+w]; cur(i) = cur(i) + w;
            end
        end
    end
    fig = figure('Position', [100 100 560 540]); hold on;
    for i = 1:n                                % ribbons
        for j = 1:n
            if F(i, j) > 0
                a1 = seg_o(i, j, 1); a2 = seg_o(i, j, 2);
                b1 = seg_i(j, i, 1); b2 = seg_i(j, i, 2);
                poly = [arc_pts(a1, a2, 0.96); chord_pts(a2, b1, 0.96); ...
                        arc_pts(b1, b2, 0.96); chord_pts(b2, a1, 0.96)];
                fill(poly(:, 1), poly(:, 2), palette('cat', i), ...
                     'FaceAlpha', 0.45, 'EdgeColor', 'none');
            end
        end
    end
    for k = 1:n                                % node arc bands + labels
        band = [arc_pts(starts(k), starts(k)+span(k), 1.0); ...
                arc_pts(starts(k)+span(k), starts(k), 1.09)];
        fill(band(:, 1), band(:, 2), palette('cat', k), 'EdgeColor', 'none');
        mid = starts(k) + span(k)/2;
        text(1.26*cos(mid), 1.26*sin(mid), sprintf('N%d', k), ...
             'HorizontalAlignment', 'center', 'FontSize', 9);
    end
    xlim([-1.55 1.55]); ylim([-1.55 1.55]);
    axis equal; axis off;
    title('Chord diagram of flows', 'FontSize', 11);
end

function p = arc_pts(t1, t2, r)
    a = linspace(t1, t2, 40)';
    p = [r*cos(a), r*sin(a)];
end

function p = chord_pts(t1, t2, r)
    p0 = r*[cos(t1), sin(t1)];
    p1 = r*[cos(t2), sin(t2)];
    t = linspace(0, 1, 40)';
    p = (1-t).^2.*p0 + t.^2.*p1;
end
