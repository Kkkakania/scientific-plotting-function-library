function fig = ga_evolution()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    n_gen = 100;
    best = 1 ./ (1 + 0.1*(0:n_gen-1));
    avg = best + 0.2 + 0.05*randn(1, n_gen);
    worst = best + 0.6 + 0.15*randn(1, n_gen);
    g = 0:n_gen-1;
    fig = figure;
    fill([g fliplr(g)], [best fliplr(worst)], palette('cat',1), 'FaceAlpha', 0.15, 'EdgeColor','none'); hold on;
    plot(g, best, 'Color', palette('cat',1), 'LineWidth', 1.5);
    plot(g, avg, '--', 'Color', palette('cat',2), 'LineWidth', 1.5);
    plot(g, worst, ':', 'Color', palette('cat',3), 'LineWidth', 1.5);
    xlabel('generation'); ylabel('fitness'); title('GA fitness evolution');
    legend({'envelope','best','mean','worst'}); grid on;
end
