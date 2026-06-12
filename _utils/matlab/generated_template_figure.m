function fig = generated_template_figure(kind, seed, title_text, domain, topic)
%GENERATED_TEMPLATE_FIGURE Shared renderer for large clean-room expansion.
%   The public wrappers pass semantic metadata only. All demo data is synthetic
%   and deterministic.
    if nargin < 2 || isempty(seed), seed = 1; end
    if nargin < 3 || isempty(title_text), title_text = ''; end
    if nargin < 4, domain = 'domain'; end
    if nargin < 5, topic = 'topic'; end
    apply_theme();
    rng(seed);
    kind = lower(kind);

    switch kind
        case 'band_timeseries'
            [x, y] = local_series(seed, 120, 1);
            y = y(1, :); w = linspace(0.25, 0.85, numel(x));
            fig = figure; hold on;
            fill([x fliplr(x)], [y-w fliplr(y+w)], palette('cat', seed), ...
                 'FaceAlpha', 0.18, 'EdgeColor', 'none');
            plot(x, y, 'Color', palette('cat', seed+1), 'LineWidth', 1.6);
            xlabel('sample'); ylabel('value'); legend({'expected range', topic}, 'Location', 'best');

        case 'control_limit'
            [x, y] = local_series(seed, 100, 1);
            y = y(1, :); if mod(seed, 3) == 0, y = y + linspace(0, 1.2, numel(x)); end
            center = mean(y(1:35)); sigma = std(y(1:35));
            fig = figure; hold on;
            plot(x, y, '-o', 'Color', palette('cat', 1), 'MarkerSize', 3);
            for m = [0 2 -2 3 -3]
                if abs(m) == 3, ls = ':'; col = palette('cat', 2); else, ls = '--'; col = [0.45 0.45 0.45]; end
                if m == 0, ls = '-'; end
                yline(center + m*sigma, ls, 'Color', col, 'LineWidth', 1);
            end
            bad = abs(y-center) > 3*sigma;
            scatter(x(bad), y(bad), 28, palette('cat', 2), 'filled');
            xlabel('sample'); ylabel('statistic');

        case 'heatmap'
            rows = 9; cols = 12;
            [C, R] = meshgrid(linspace(-1, 1, cols), linspace(-1, 1, rows));
            Z = exp(-2.8*((R-0.25).^2 + (C+0.15).^2)) + 0.25*randn(rows, cols);
            fig = figure; imagesc(Z); axis tight; colorbar; colormap(parula);
            xlabel('condition'); ylabel('channel');

        case 'contour'
            [X, Y] = meshgrid(linspace(-3, 3, 90), linspace(-2.5, 2.5, 80));
            Z = sin(X*(1 + mod(seed, 5)/8)).*cos(Y) + 0.25*X - 0.12*Y.^2;
            fig = figure; contourf(X, Y, Z, 14, 'LineStyle', 'none'); hold on;
            contour(X, Y, Z, 8, 'k', 'LineWidth', 0.35); colorbar;
            xlabel('x'); ylabel('y');

        case 'scatter_cluster'
            fig = figure; hold on;
            A = [0.22 0.06; 0.02 0.36];
            for i = 1:4
                mu = [cos((i-1)*1.6), sin((i-1)*1.6)]*(1.2 + 0.1*(i-1));
                pts = randn(55, 2)*A + mu;
                scatter(pts(:,1), pts(:,2), 22, palette('cat', i), 'filled', ...
                        'MarkerFaceAlpha', 0.78);
            end
            xlabel('feature 1'); ylabel('feature 2');

        case 'rank_bar'
            values = sort(lognrnd(0, 0.45, [1 8]), 'descend');
            fig = figure; barh(values, 'FaceColor', 'flat'); ax = gca;
            for i = 1:numel(values), ax.Children.CData(i,:) = palette('cat', i); end
            set(gca, 'YDir', 'reverse', 'YTick', 1:8, 'YTickLabel', local_labels('item', 8));
            xlabel('score');

        case 'radar'
            n = 6; theta = linspace(0, 2*pi, n+1);
            fig = figure; pax = polaraxes; hold(pax, 'on');
            for i = 1:3
                vals = 0.45 + 0.45*rand(1, n); vals = [vals vals(1)];
                polarplot(pax, theta, vals, 'Color', palette('cat', i), 'LineWidth', 1.5);
            end
            pax.RLim = [0 1];

        case 'waterfall'
            steps = 0.15 + 0.75*randn(1, 10); cum = [0 cumsum(steps)];
            fig = figure; hold on;
            for i = 1:numel(steps)
                if steps(i) >= 0, col = palette('cat', 3); else, col = palette('cat', 2); end
                bar(i, abs(steps(i)), 0.65, 'BaseValue', min(cum(i), cum(i+1)), ...
                    'FaceColor', col, 'EdgeColor', 'none');
                plot([i-0.32 i+0.32], [cum(i+1) cum(i+1)], 'Color', [0.35 0.35 0.35]);
            end
            yline(0, '-', 'Color', [0.25 0.25 0.25]); xlabel('step'); ylabel('cumulative change');

        case 'small_multiples'
            [x, y] = local_series(seed, 72, 6);
            fig = figure; tl = tiledlayout(2, 3, 'TileSpacing', 'compact');
            for i = 1:6
                ax = nexttile(tl); plot(ax, x, y(i,:), 'Color', palette('cat', i)); hold(ax, 'on');
                yline(ax, mean(y(i,:)), ':', 'Color', [0.45 0.45 0.45]);
                title(ax, sprintf('scenario %d', i), 'FontSize', 8);
            end
            xlabel(tl, 'sample'); ylabel(tl, 'value');

        case 'polar_profile'
            theta = linspace(0, 2*pi, 240);
            r = 1 + 0.28*cos((2 + mod(seed, 4))*theta) + 0.12*sin(5*theta + seed);
            fig = figure; polarplot(theta, r, 'Color', palette('cat', seed), 'LineWidth', 1.5);

        case 'phase_plane'
            [X, Y] = meshgrid(linspace(-2.4, 2.4, 28), linspace(-2.0, 2.0, 24));
            U = Y; V = -0.6*X - 0.2*Y + 0.08*sin(seed + X.*Y);
            fig = figure; quiver(X, Y, U, V, 'Color', palette('cat', seed));
            xlabel('state x1'); ylabel('state x2');

        case 'distribution'
            a = randn(1, 600); b = 0.45 + 0.75*randn(1, 600);
            fig = figure; hold on;
            histogram(a, 32, 'Normalization', 'pdf', 'FaceAlpha', 0.45, 'FaceColor', palette('cat', 1));
            histogram(b, 32, 'Normalization', 'pdf', 'FaceAlpha', 0.45, 'FaceColor', palette('cat', 2));
            xline(mean(b), 'Color', palette('cat', 2), 'LineWidth', 1.5);
            xlabel('value'); ylabel('density');

        case 'bubble_matrix'
            m = 7; n = 7; [X, Y] = meshgrid(1:n, 1:m); val = 2*rand(m, n)-1;
            fig = figure; scatter(X(:), Y(:), 60 + 420*abs(val(:)), val(:), 'filled');
            colormap(parula); colorbar; xlabel('condition'); ylabel('row');

        case 'lollipop'
            vals = sort(0.2 + 0.8*rand(1, 9));
            fig = figure; hold on;
            for i = 1:numel(vals)
                plot([0 vals(i)], [i i], '-', 'Color', [0.70 0.70 0.70]);
                scatter(vals(i), i, 50, palette('cat', i), 'filled');
            end
            set(gca, 'YTick', 1:9, 'YTickLabel', local_labels('factor', 9)); xlabel('importance');

        case 'interval_forest'
            mid = 0.5*randn(1, 9); lo = mid - (0.15 + 0.4*rand(1, 9)); hi = mid + (0.15 + 0.4*rand(1, 9));
            fig = figure; hold on;
            for i = 1:9
                plot([lo(i) hi(i)], [i i], '-', 'Color', palette('cat', seed), 'LineWidth', 1.4);
                scatter(mid(i), i, 28, palette('cat', seed), 'filled');
            end
            xline(0, '--', 'Color', [0.35 0.35 0.35]); set(gca, 'YTick', 1:9, 'YTickLabel', local_labels('study', 9)); xlabel('effect');

        case 'stacked_area'
            x = 1:80; y = gamrnd(2.0, 0.35, [4, numel(x)]);
            y = cumsum(y, 2); y = y ./ max(y, [], 2);
            fig = figure; area(x, y'); xlabel('sample'); ylabel('share');

        case 'step_curve'
            x = 1:16; y = cumsum(randi([-2 4], 1, numel(x)));
            fig = figure; stairs(x, y, 'Color', palette('cat', seed), 'LineWidth', 1.8); hold on;
            scatter(x, y, 24, palette('cat', seed+1), 'filled'); xlabel('stage'); ylabel('state');

        case 'surface3d'
            [X, Y] = meshgrid(linspace(-2.6, 2.6, 54));
            Z = sin(X*(1 + mod(seed, 4)*0.15)).*cos(Y).*exp(-0.08*(X.^2 + Y.^2));
            fig = figure; surf(X, Y, Z, 'EdgeColor', 'none'); colormap(parula);
            xlabel('x'); ylabel('y'); zlabel('response'); view(42, 28);

        case 'calendar_grid'
            data = randn(7, 18) + linspace(-0.8, 0.8, 18);
            fig = figure; imagesc(data); colorbar; colormap(parula);
            set(gca, 'YTick', 1:7, 'YTickLabel', {'Mon','Tue','Wed','Thu','Fri','Sat','Sun'}); xlabel('week');

        case 'slope'
            a = 0.2 + 0.7*rand(1, 8); b = a + 0.05 + 0.22*randn(1, 8);
            fig = figure; hold on;
            for i = 1:8, plot([1 2], [a(i) b(i)], '-o', 'Color', palette('cat', i)); end
            xlim([0.7 2.3]); set(gca, 'XTick', [1 2], 'XTickLabel', {'before','after'}); ylabel('metric');

        case 'decision_map'
            [X, Y] = meshgrid(linspace(-3, 3, 120), linspace(-3, 3, 100));
            Z = tanh(0.8*X - 0.4*Y + 0.35*sin(seed + X.*Y));
            pts = randn(140, 2);
            fig = figure; contourf(X, Y, Z, 15, 'LineStyle', 'none'); hold on; colormap(parula);
            scatter(pts(:,1), pts(:,2), 16, pts(:,1)-pts(:,2)>0, 'filled'); xlabel('feature 1'); ylabel('feature 2');

        otherwise
            error('unknown generated pattern kind: %s', kind);
    end

    if isempty(title_text), title_text = sprintf('%s: %s', domain, topic); end
    title(title_text, 'Interpreter', 'none');
    grid on;
end

function [x, y] = local_series(seed, n, k)
    rng(seed);
    x = 1:n;
    base = cumsum(0.12*randn(1, n)) + sin(linspace(0, 5.8, n));
    y = zeros(k, n);
    for i = 1:k
        drift = 0.015*(i-2)*x;
        seasonal = 0.25*sin(linspace(0, 4*pi, n) + (i-1)*0.6);
        y(i,:) = base + drift + seasonal + (0.08 + 0.02*(i-1))*randn(1, n);
    end
end

function labels = local_labels(prefix, n)
    labels = cell(1, n);
    for i = 1:n, labels{i} = sprintf('%s %d', prefix, i); end
end
