function fig = training_curves()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    e = 1:100;
    tr_loss = 2.5*exp(-e/30) + 0.1 + 0.04*randn(1,100);
    va_loss = 2.5*exp(-e/30) + 0.25 + 0.08*randn(1,100);
    fig = figure('Position',[100 100 800 450]);
    subplot(1,2,1);
    plot(e, tr_loss, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot(e, va_loss, 'Color', palette('cat',2), 'LineWidth', 1.5);
    xlabel('epoch'); ylabel('loss'); legend({'train','val'}); grid on;
    subplot(1,2,2);
    plot(e, 1 - tr_loss/3, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot(e, 1 - va_loss/3, 'Color', palette('cat',2), 'LineWidth', 1.5);
    xlabel('epoch'); ylabel('accuracy'); grid on;
    sgtitle('Training curves');
end
