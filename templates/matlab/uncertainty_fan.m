function fig = uncertainty_fan()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3); c = palette('cat',1);
    x = 0:49;
    sims = cumsum(randn(500, 50), 2);
    p = prctile(sims, [5 25 50 75 95], 1);
    fig = figure;
    fill([x, fliplr(x)], [p(1,:), fliplr(p(5,:))], c, 'FaceAlpha', 0.15, 'EdgeColor','none'); hold on;
    fill([x, fliplr(x)], [p(2,:), fliplr(p(4,:))], c, 'FaceAlpha', 0.30, 'EdgeColor','none');
    plot(x, p(3,:), 'Color', c, 'LineWidth', 1.5);
    xlabel('t'); ylabel('value'); title('Uncertainty fan');
    legend({'5-95%','25-75%','median'}); grid on;
end
