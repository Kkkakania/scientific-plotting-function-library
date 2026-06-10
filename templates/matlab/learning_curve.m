function fig = learning_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = round(logspace(1, 3.5, 12));
    train = 0.05 + 0.3./sqrt(n) + 0.01*randn(size(n));
    valid = 0.18 + 0.5./sqrt(n) + 0.02*randn(size(n));
    fig = figure;
    semilogx(n, train, '-o', 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    semilogx(n, valid, '-s', 'Color', palette('cat',2), 'LineWidth', 1.5);
    xlabel('training set size'); ylabel('error'); title('Learning curve');
    legend({'train','validation'}); grid on;
end
