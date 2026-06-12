function fig = bootstrap_ci()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    n = 60; n_boot = 4000;
    data = -1.5*(log(rand(n, 1)) + log(rand(n, 1)));   % Gamma(shape=2, scale=1.5)
    theta_hat = mean(data);
    idx = randi(n, n_boot, n);
    boot = mean(data(idx), 2);
    [lo, hi] = bca_interval(data, boot, theta_hat, 0.05);
    fig = figure; hold on;
    histogram(boot, 40, 'Normalization', 'pdf', 'FaceColor', palette('cat', 1), ...
              'FaceAlpha', 0.75, 'EdgeColor', 'w', 'LineWidth', 0.3);
    h1 = xline(theta_hat, '-', 'Color', palette('cat', 2), 'LineWidth', 1.5);
    h2 = xline(lo, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 1.1);
    xline(hi, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 1.1);
    xlabel('bootstrap statistic (mean)'); ylabel('density');
    title('Bootstrap distribution of the mean');
    legend([h1 h2], {sprintf('sample mean = %.2f', theta_hat), ...
           sprintf('BCa 95%% CI [%.2f, %.2f]', lo, hi)}, 'Location', 'northeast');
    grid on;
end

function [lo, hi] = bca_interval(data, boot, theta_hat, alpha)
    z0 = sqrt(2)*erfinv(2*mean(boot < theta_hat) - 1);
    n = numel(data);
    jack = (sum(data) - data) / (n - 1);    % leave-one-out means
    d = mean(jack) - jack;
    a = sum(d.^3) / (6*(sum(d.^2))^1.5);
    z = sqrt(2)*erfinv(2*[alpha/2, 1-alpha/2] - 1);
    p = 0.5*erfc(-(z0 + (z0 + z)./(1 - a*(z0 + z)))/sqrt(2));
    q = quantile_lin(boot, p);
    lo = q(1); hi = q(2);
end

function q = quantile_lin(x, p)
    xs = sort(x(:)).'; n = numel(xs);
    pos = p*(n-1) + 1;
    lo_i = min(max(floor(pos), 1), n);
    hi_i = min(max(ceil(pos), 1), n);
    q = xs(lo_i) + (pos - lo_i).*(xs(hi_i) - xs(lo_i));
end
