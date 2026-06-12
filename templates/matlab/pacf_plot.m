function fig = pacf_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    nlags = 20; n = 400;
    y = zeros(1, n);
    for i = 3:n
        y(i) = 0.6*y(i-1) - 0.3*y(i-2) + randn;   % AR(2) demo series
    end
    pacf = pacf_(y, nlags);
    ci = 1.96/sqrt(n);
    lags = 1:nlags;
    fig = figure; hold on;
    hci = fill([0 nlags+1 nlags+1 0], [-ci -ci ci ci], palette('cat',1), ...
               'FaceAlpha', 0.15, 'EdgeColor', 'none');
    plot([0 nlags+1], [0 0], 'Color', [0.4 0.4 0.4], 'LineWidth', 0.8);
    xs = [lags; lags; nan(1, nlags)];
    ys = [zeros(1, nlags); pacf; nan(1, nlags)];
    plot(xs(:), ys(:), 'Color', palette('cat',1), 'LineWidth', 1.5);
    plot(lags, pacf, 'o', 'Color', palette('cat',2), 'MarkerSize', 4, ...
         'MarkerFaceColor', palette('cat',2), 'LineStyle', 'none');
    xlim([0 nlags+1]);
    xlabel('lag'); ylabel('partial autocorrelation');
    title('Partial autocorrelation (AR(2) demo)');
    legend(hci, {'95% confidence band'});
    grid on;
end

function pacf = pacf_(y, nlags)
    % Durbin-Levinson recursion on the sample autocorrelation
    y = y - mean(y);
    n = numel(y);
    r = zeros(1, nlags + 1);
    for k = 0:nlags
        r(k+1) = sum(y(1:n-k).*y(1+k:n));
    end
    r = r / r(1);
    phi = zeros(nlags + 1, nlags + 1);        % phi(k+1, j+1) ~ phi_{k,j}
    phi(2, 2) = r(2);
    for k = 2:nlags
        num = r(k+1) - phi(k, 2:k)*fliplr(r(2:k))';
        den = 1 - phi(k, 2:k)*r(2:k)';
        phi(k+1, k+1) = num/den;
        phi(k+1, 2:k) = phi(k, 2:k) - phi(k+1, k+1)*fliplr(phi(k, 2:k));
    end
    pacf = diag(phi)';
    pacf = pacf(2:end);
end
