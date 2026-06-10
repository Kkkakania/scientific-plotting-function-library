function fig = phase_margin()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    w = logspace(-1, 3, 1000); s = 1j*w;
    G = 10 ./ (s .* (s/5 + 1) .* (s/50 + 1));
    mag = 20*log10(abs(G)); phs = unwrap(angle(G))*180/pi;
    [~, igc] = min(abs(mag));
    [~, ipc] = min(abs(phs + 180));
    PM = 180 + phs(igc); GM = -mag(ipc);
    fig = figure('Position',[100 100 700 550]);
    subplot(2,1,1); semilogx(w, mag, 'Color', palette('cat',1)); hold on;
    yline(0, 'Color', [0.5 0.5 0.5]);
    plot([w(ipc) w(ipc)], [-GM 0], 'r', 'LineWidth', 2);
    text(w(ipc)*1.2, -GM/2, sprintf('GM = %.1f dB', GM), 'Color', 'r');
    ylabel('mag (dB)'); title('Gain/phase margin'); grid on;
    subplot(2,1,2); semilogx(w, phs, 'Color', palette('cat',1)); hold on;
    yline(-180, 'Color', [0.5 0.5 0.5]);
    plot([w(igc) w(igc)], [-180 phs(igc)], 'r', 'LineWidth', 2);
    text(w(igc)*1.2, (-180+phs(igc))/2, sprintf('PM = %.1f°', PM), 'Color', 'r');
    xlabel('\omega (rad/s)'); ylabel('phase (°)'); grid on;
end
