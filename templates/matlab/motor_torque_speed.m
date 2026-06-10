function fig = motor_torque_speed()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    R2 = 0.08; X = 0.45; freqs = [10 20 30 40 50];
    cmap = sci_palettes('blues', numel(freqs) + 3);
    fig = figure; hold on;
    for i = 1:numel(freqs)
        f = freqs(i); ws = f/50;
        w = linspace(0, ws, 300);
        s = min(max((ws - w)/max(ws, 1e-6), 1e-4), 1);
        T = (R2./s) ./ ((R2./s).^2 + (X*f/50)^2);
        T = T/max(T)*2.0;
        plot(w*1500, T, 'Color', cmap(i+2, :), 'DisplayName', sprintf('%d Hz', f));
    end
    plot([0 1500], [1 1], '--', 'Color', palette('cat',2), 'LineWidth', 1, ...
         'DisplayName', 'load torque');
    xlabel('speed (rpm)'); ylabel('torque (p.u.)');
    title('Induction motor torque-speed (V/f control)');
    legend('FontSize', 7, 'Location', 'northwest'); grid on;
end
