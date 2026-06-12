function fig = qq_compare_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    n = 300;
    samples = {randn(n, 1), ...                                   % normal
               randn(n, 1) ./ sqrt(sum(randn(n, 3).^2, 2) / 3), ... % Student t df=3
               exp(0.6 * randn(n, 1)), ...                        % log-normal
               2*rand(n, 1) - 1};                                 % uniform
    names = {'Normal', 'Student t (df=3)', 'Log-normal (skewed)', 'Uniform'};
    p = ((1:n)' - 0.5) / n;
    q_theo = sqrt(2) * erfinv(2*p - 1);              % normal quantiles, no toolbox
    fig = figure('Position',[100 100 660 600]);
    for i = 1:4
        x = samples{i};
        z = sort((x - mean(x)) / std(x));
        subplot(2, 2, i); hold on;
        scatter(q_theo, z, 10, palette('cat',i), 'filled', 'MarkerFaceAlpha', 0.6);
        lim = [min(min(q_theo), min(z)), max(max(q_theo), max(z))];
        plot(lim, lim, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
        title(names{i});
        xlabel('theoretical quantiles'); ylabel('sample quantiles');
        grid on;
    end
    sgtitle('Q-Q plots vs normal');
end
