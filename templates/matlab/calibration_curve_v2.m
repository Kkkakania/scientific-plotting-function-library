function fig = calibration_curve_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(21);
    n = 3000;
    p_true = median(rand(3, n), 1);            % Beta(2,2) via order statistics
    y = double(rand(1, n) < p_true);
    p_good = min(max(p_true + 0.06*randn(1, n), 0.001), 0.999);
    z = 1.8*log(p_true./(1 - p_true));         % over-confident model
    p_over = 1./(1 + exp(-z));
    fig = figure('Position', [100 100 500 560]);
    tl = tiledlayout(4, 1, 'TileSpacing', 'compact');
    ax = nexttile(tl, [3 1]); hold(ax, 'on');
    hp = plot(ax, [0 1], [0 1], '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
    ps = {p_good, p_over}; names = {'calibrated', 'over-confident'};
    hh = gobjects(1, 2);
    for i = 1:2
        [mids, obs] = reliability(y, ps{i}, 10);
        hh(i) = plot(ax, mids, obs, '-o', 'Color', palette('cat', i), ...
                     'MarkerSize', 4, 'MarkerFaceColor', palette('cat', i));
    end
    ylabel(ax, 'observed frequency'); title(ax, 'Calibration (reliability) diagram');
    legend(ax, [hp hh], [{'perfect'}, names], 'Location', 'northwest');
    grid(ax, 'on'); set(ax, 'XTickLabel', []);
    axh = nexttile(tl); hold(axh, 'on');
    edges = linspace(0, 1, 21);
    cnt1 = histcounts(p_good, edges);
    cnt2 = histcounts(p_over, edges);
    ctr = (edges(1:end-1) + edges(2:end))/2;
    hb = bar(axh, ctr, [cnt1; cnt2]', 1, 'grouped', 'EdgeColor', 'none');
    hb(1).FaceColor = palette('cat', 1); hb(2).FaceColor = palette('cat', 2);
    hb(1).FaceAlpha = 0.8; hb(2).FaceAlpha = 0.8;
    xlabel(axh, 'predicted probability'); ylabel(axh, 'count');
    axh.YGrid = 'on'; axh.XGrid = 'off';
end

function [mids, obs] = reliability(y, p, n_bins)
    edges = linspace(0, 1, n_bins+1);
    idx = min(max(discretize(p, edges), 1), n_bins);
    mids = []; obs = [];
    for b = 1:n_bins
        m = idx == b;
        if sum(m) >= 5
            mids(end+1) = mean(p(m)); %#ok<AGROW>
            obs(end+1) = mean(y(m));  %#ok<AGROW>
        end
    end
end
