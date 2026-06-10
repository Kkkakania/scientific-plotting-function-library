function fig = vswr_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = linspace(1.5, 3.0, 400); f0 = 2.4;
    gamma = 0.05 + 0.8*exp(-((f - f0)/0.05).^2);
    vswr = (1 + gamma) ./ (1 - gamma + 1e-9);
    rl = -20*log10(gamma + 1e-9);
    fig = figure;
    yyaxis left;
    plot(f, vswr, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    yline(2, '--', 'Color', [0.5 0.5 0.5]);
    ylabel('VSWR');
    yyaxis right;
    plot(f, rl, '--', 'Color', palette('cat',2), 'LineWidth', 1.5);
    set(gca,'YDir','reverse'); ylabel('return loss (dB)');
    xlabel('frequency (GHz)'); title('VSWR vs frequency'); grid on;
end
