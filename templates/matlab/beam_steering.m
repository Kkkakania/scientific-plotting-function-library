function fig = beam_steering()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 8; d = 0.6; steer = [0 30 60]; floor_db = -35;
    theta = linspace(-90, 90, 1801);
    st = sind(theta);
    fig = figure; hold on;
    hh = gobjects(1, numel(steer));
    for i = 1:numel(steer)
        s0 = steer(i);
        psi = 2*pi*d*(st - sind(s0));
        den = n*sin(psi/2);
        af = abs(sin(n*psi/2) ./ den);
        af(abs(den) < 1e-9) = 1.0;
        db = min(max(20*log10(af + 1e-9), floor_db), 0);
        c = palette('cat', i);
        hh(i) = plot(theta, db, 'Color', c, 'LineWidth', 1.5);
        xline(s0, ':', 'Color', c, 'LineWidth', 1);
    end
    % grating lobe of the 60-deg beam: sin(tg) = sin(60) - 1/d
    c3 = palette('cat', 3);
    tg = asind(sind(60) - 1/d);
    plot([tg+7, tg+0.5], [-7.2, -2.2], '-', 'Color', c3, 'LineWidth', 1);
    text(tg+8, -8, 'grating lobe', 'FontSize', 8, 'Color', c3);
    yline(-13.2, '--', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
    text(-88, -12.6, 'first sidelobe level', 'FontSize', 7, 'Color', [0.5 0.5 0.5]);
    xlim([-90 90]); ylim([floor_db 2]);
    xlabel('angle (deg)'); ylabel('array factor (dB)');
    title('Beam steering, N=8 ULA (d=0.6\lambda)');
    legend(hh, {'steer 0^\circ', 'steer 30^\circ', 'steer 60^\circ'}, ...
           'Location', 'southwest');
    grid on;
end
