function fig = residual_history()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 2000; it = 1:n;
    names = {'continuity','u-velocity','v-velocity','k','epsilon'};
    taus = [600 400 400 300 350]; bases = [1 0.5 0.4 0.8 0.6];
    fig = figure; hold on;
    for i = 1:5
        res = bases(i) * exp(-it/taus(i)) .* (1 + 0.1*randn(1,n));
        semilogy(it, abs(res), 'Color', palette('cat',i), 'LineWidth', 1);
    end
    set(gca,'YScale','log');
    yline(1e-4, '--', 'Color',[0.5 0.5 0.5]);
    xlabel('iteration'); ylabel('residual'); title('Residual history');
    legend(names, 'FontSize', 7); grid on;
end
