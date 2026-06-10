function fig = calibration_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(12); c = palette('cat',1);
    n = 2000; pt = rand(n,1);
    y = rand(n,1) < pt; pp = min(max(pt + 0.1*randn(n,1), 0), 1);
    edges = linspace(0, 1, 11);
    mids = (edges(1:end-1) + edges(2:end))/2; obs = nan(1,10);
    for i = 1:10
        mask = pp >= edges(i) & pp < edges(i+1);
        if any(mask), obs(i) = mean(y(mask)); end
    end
    fig = figure;
    plot([0 1], [0 1], '--', 'Color', [0.5 0.5 0.5]); hold on;
    plot(mids, obs, '-o', 'Color', c, 'LineWidth', 1.5, 'MarkerFaceColor', c);
    xlabel('predicted probability'); ylabel('observed frequency');
    title('Calibration curve'); legend({'ideal','model'}); grid on;
end
