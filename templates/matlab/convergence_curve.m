function fig = convergence_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    n = 200; it = 1:n;
    names = {'GD','Momentum','Adam','L-BFGS'};
    taus = [80 50 30 25];
    fig = figure; hold on;
    for i = 1:4
        cur = 10 * exp(-it/taus(i)) + 0.05 + 0.1*exp(-it/10).*abs(randn(1,n));
        semilogy(it, cur, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    set(gca,'YScale','log');
    xlabel('iteration'); ylabel('loss'); title('Convergence comparison');
    legend(names); grid on;
end
