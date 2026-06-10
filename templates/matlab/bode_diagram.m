function fig = bode_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    wn = 2*pi*100; w = logspace(0,4,500)*2*pi;
    zetas = [0.1 0.3 0.707 1.5];
    fig = figure('Position',[100 100 800 550]);
    subplot(2,1,1); hold on;
    for k = 1:numel(zetas)
        s = 1j*w; z = zetas(k);
        H = wn^2 ./ (s.^2 + 2*z*wn*s + wn^2);
        semilogx(w/(2*pi), 20*log10(abs(H)), 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    set(gca,'XScale','log'); yline(-3,'--','Color',[0.5 0.5 0.5]);
    ylabel('magnitude (dB)'); title('Bode diagram');
    legend(arrayfun(@(z)sprintf('\\zeta=%.3g',z),zetas,'UniformOutput',false)); grid on;
    subplot(2,1,2); hold on;
    for k = 1:numel(zetas)
        s = 1j*w; z = zetas(k);
        H = wn^2 ./ (s.^2 + 2*z*wn*s + wn^2);
        semilogx(w/(2*pi), unwrap(angle(H))*180/pi, 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    set(gca,'XScale','log'); xlabel('frequency (Hz)'); ylabel('phase (deg)');
    yticks([-180 -135 -90 -45 0]); grid on;
end
