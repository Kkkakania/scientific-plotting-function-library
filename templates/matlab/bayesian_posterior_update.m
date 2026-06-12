function fig = bayesian_posterior_update()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    a0 = 2; b0 = 2;
    th = linspace(0.001, 0.999, 500);
    % stages: prior -> 10 trials (7 successes) -> cumulative 50 trials (32 successes)
    stages = [a0, b0; a0+7, b0+3; a0+32, b0+18];
    names = {'prior  Beta(2, 2)', 'after 10 trials (7 successes)', ...
             'after 50 trials (32 successes)'};
    fig = figure; hold on;
    hh = gobjects(1, 3);
    for i = 1:3
        a = stages(i, 1); b = stages(i, 2);
        pdf = exp((a-1)*log(th) + (b-1)*log(1-th) - betaln(a, b));
        c = palette('cat', i);
        hh(i) = plot(th, pdf, 'Color', c, 'LineWidth', 1.5);
        fill([th, fliplr(th)], [pdf, zeros(size(pdf))], c, ...
             'FaceAlpha', 0.18, 'EdgeColor', 'none');
        mode_i = (a-1)/(a+b-2);
        xline(mode_i, ':', 'Color', c, 'LineWidth', 0.9);
    end
    xlabel('success probability \theta'); ylabel('density');
    title('Bayesian updating (Beta-Binomial)');
    legend(hh, names, 'Location', 'northwest');
    grid on;
end
