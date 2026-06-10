function fig = validation_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    param = logspace(-2, 2, 20);
    train = 0.4 - 0.35 ./ (1 + 0.5./param);
    valid = train + 0.05 + 0.2*((log10(param) - 0.5).^2);
    train_std = 0.02 + 0.02*rand(1, 20);
    valid_std = 0.04 + 0.03*rand(1, 20);
    fig = figure;
    fill([param fliplr(param)], [train-train_std fliplr(train+train_std)], ...
         palette('cat',1), 'FaceAlpha', 0.2, 'EdgeColor','none'); hold on;
    fill([param fliplr(param)], [valid-valid_std fliplr(valid+valid_std)], ...
         palette('cat',2), 'FaceAlpha', 0.2, 'EdgeColor','none');
    semilogx(param, train, '-o', 'Color', palette('cat',1), 'LineWidth', 1.5);
    semilogx(param, valid, '-s', 'Color', palette('cat',2), 'LineWidth', 1.5);
    set(gca,'XScale','log');
    xlabel('hyperparameter'); ylabel('error');
    title('Validation curve'); legend({'','','train','validation'}); grid on;
end
