function fig = ewma_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(10);
    lam = 0.2; L = 3.0;
    n = 60; mu = 50.0; sigma = 2.0;
    x = mu + sigma*randn(1, n);
    x(41:end) = x(41:end) + 1.2*sigma;        % inject a sustained drift
    z = zeros(1, n); prev = mu;
    for i = 1:n
        prev = lam*x(i) + (1 - lam)*prev;
        z(i) = prev;
    end
    i1 = 1:n;
    half = L*sigma*sqrt(lam/(2 - lam) * (1 - (1 - lam).^(2*i1)));
    ucl = mu + half; lcl = mu - half;
    t = 0:n-1;
    fig = figure; hold on;
    fill([t fliplr(t)], [lcl fliplr(ucl)], palette('cat',1), ...
         'FaceAlpha', 0.10, 'EdgeColor', 'none');
    hraw = plot(t, x, '.', 'Color', palette('cat',8), 'MarkerSize', 8);
    hz = plot(t, z, '-o', 'Color', palette('cat',1), 'MarkerSize', 3.5, ...
              'MarkerFaceColor', palette('cat',1));
    hcl = plot(t, ucl, '--', 'Color', palette('cat',8), 'LineWidth', 1);
    plot(t, lcl, '--', 'Color', palette('cat',8), 'LineWidth', 1);
    htg = plot([0 n-1], [mu mu], '-', 'Color', palette('cat',3), 'LineWidth', 1);
    out = z > ucl | z < lcl;
    hout = plot(t(out), z(out), 'o', 'Color', palette('cat',2), ...
                'MarkerSize', 6, 'LineWidth', 1.2, 'LineStyle', 'none');
    xlabel('sample number'); ylabel('value');
    title(sprintf('EWMA control chart (\\lambda=%.1f)', lam));
    legend([hraw hz hcl htg hout], ...
           {'raw observation', 'EWMA', 'UCL / LCL', 'target', 'out of control'}, ...
           'Location', 'northwest', 'FontSize', 7);
    grid on;
end
