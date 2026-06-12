function fig = mcmc_trace_panel()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(15);
    names = {'\mu', '\sigma'};
    targets = [2.0 1.2]; sds = [0.4 0.2];
    n_chain = 4; n_iter = 600; warm = 100;
    fig = figure('Position', [100 100 700 480]);
    for r = 1:2
        ch = make_chains(targets(r), sds(r), n_chain, n_iter);
        ax1 = subplot(2, 3, [(r-1)*3+1, (r-1)*3+2]); hold(ax1, 'on');
        ax2 = subplot(2, 3, (r-1)*3+3); hold(ax2, 'on');
        post = ch(:, warm+1:end);
        grid_v = linspace(min(post(:)), max(post(:)), 200);
        for c = 1:n_chain
            col = palette('cat', c);
            plot(ax1, 1:n_iter, ch(c, :), 'Color', col, 'LineWidth', 0.6);
            plot(ax2, grid_v, kde_(ch(c, warm+1:end), grid_v), ...
                 'Color', col, 'LineWidth', 1.0);
        end
        yl = ylim(ax1);                       % warm-up shading
        fill(ax1, [0 warm warm 0], [yl(1) yl(1) yl(2) yl(2)], [0.5 0.5 0.5], ...
             'FaceAlpha', 0.15, 'EdgeColor', 'none');
        ylim(ax1, yl); xlim(ax1, [0 n_iter]);
        ylabel(ax1, names{r});
        title(ax1, sprintf('trace: %s', names{r}), 'FontSize', 9);
        title(ax2, sprintf('posterior: %s', names{r}), 'FontSize', 9);
        ylabel(ax2, 'density');
        grid(ax1, 'on'); grid(ax2, 'on');
        if r == 2
            xlabel(ax1, 'iteration'); xlabel(ax2, 'value');
        end
    end
    sgtitle('MCMC traces and posterior densities');
end

function out = make_chains(target, sd, n_chain, n_iter)
    % AR(1) chains around the target, over-dispersed starting points
    rho = 0.85;
    out = zeros(n_chain, n_iter);
    starts = target + [-3 -1 1 3]*sd;
    for c = 1:n_chain
        e = sd*sqrt(1 - rho^2)*randn(1, n_iter);
        x = starts(c);
        for t = 1:n_iter
            x = target + rho*(x - target) + e(t);
            out(c, t) = x;
        end
    end
end

function d = kde_(samples, grid_v)
    % Gaussian KDE, Scott's rule bandwidth (no toolbox)
    m = numel(samples);
    bw = std(samples) * m^(-1/5);
    d = mean(exp(-0.5*((grid_v(:)' - samples(:))/bw).^2), 1) / (bw*sqrt(2*pi));
end
