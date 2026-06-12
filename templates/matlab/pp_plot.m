function fig = pp_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(9);
    n = 250;
    x1 = 5 + 2*randn(n, 1);                              % normal sample
    x2 = -2*log(rand(n, 1)) - 2*log(rand(n, 1));         % gamma k=2 theta=2
    data = {x1, x2};
    names = {'normal sample', 'right-skewed sample'};
    fig = figure('Position',[100 100 500 460]); hold on;
    plot([0 1], [0 1], '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
    p_emp = ((1:n)' - 0.5) / n;
    for i = 1:2
        x = data{i};
        xs = sort(x);
        mu = mean(x); sd = std(x);
        p_theo = 0.5 * (1 + erf((xs - mu) / (sd * sqrt(2))));  % fitted normal CDF
        scatter(p_theo, p_emp, 12, palette('cat',i), 'filled', ...
                'MarkerFaceAlpha', 0.6);
    end
    xlim([-0.02 1.02]); ylim([-0.02 1.02]);
    xlabel('theoretical cumulative probability');
    ylabel('empirical cumulative probability');
    title('P-P plot vs fitted normal');
    legend([{'reference'} names], 'Location', 'northwest');
    grid on;
end
