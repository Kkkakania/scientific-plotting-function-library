function fig = volatility_cone()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(15);
    n = 1000;
    vol_state = 0.010 * exp(0.4 * sin((0:n-1) / 80));
    r = randn(1, n) .* vol_state;
    windows = [5 10 21 42 63 126];
    nw = numel(windows);
    qmin = zeros(1, nw); q25 = zeros(1, nw); q50 = zeros(1, nw);
    q75 = zeros(1, nw); qmax = zeros(1, nw); current = zeros(1, nw);
    for k = 1:nw
        w = windows(k);
        c1 = conv(r, ones(1, w)/w, 'valid');
        c2 = conv(r.^2, ones(1, w)/w, 'valid');
        vol = sqrt(max(c2 - c1.^2, 0)) * sqrt(252) * 100;  % annualized %
        qmin(k) = quantile_(vol, 0.0);  q25(k) = quantile_(vol, 0.25);
        q50(k) = quantile_(vol, 0.5);   q75(k) = quantile_(vol, 0.75);
        qmax(k) = quantile_(vol, 1.0);  current(k) = vol(end);
    end
    c0 = palette('cat',1); c1c = palette('cat',2);
    fig = figure; hold on;
    h1 = fill([windows fliplr(windows)], [qmin fliplr(qmax)], c0, ...
              'FaceAlpha', 0.15, 'EdgeColor', 'none');
    h2 = fill([windows fliplr(windows)], [q25 fliplr(q75)], c0, ...
              'FaceAlpha', 0.35, 'EdgeColor', 'none');
    h3 = plot(windows, q50, '-o', 'Color', c0, 'MarkerFaceColor', c0, ...
              'MarkerSize', 4, 'LineWidth', 1.5);
    h4 = plot(windows, current, 's--', 'Color', c1c, 'MarkerFaceColor', ...
              c1c, 'MarkerSize', 5, 'LineWidth', 1.5);
    set(gca, 'XScale', 'log', 'XTick', windows, 'XTickLabel', windows);
    xlabel('window length (days)');
    ylabel('annualized volatility (%)');
    title('Volatility cone');
    legend([h1 h2 h3 h4], {'min-max', '25-75%', 'median', 'current'}, ...
           'Box', 'off');
    grid on;
end

function v = quantile_(x, q)
    % linear-interpolation quantile, matches numpy default
    xs = sort(x(:));
    m = numel(xs);
    h = (m - 1) * q + 1;
    lo = floor(h); hi = ceil(h);
    v = xs(lo) + (h - lo) * (xs(hi) - xs(lo));
end
