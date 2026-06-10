function fig = dq_current_locus()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    id_ss = -12; iq_ss = 35;                       % steady-state operating point (A)
    % start-up transient: damped spiral from (0,0) converging to steady point
    t = linspace(0, 0.12, 800);
    z_ss = id_ss + 1i*iq_ss;
    z = z_ss*(1 - exp(-(35 + 1i*2*pi*60)*t));
    % MTPA curve (dashed), parabolic approximation through the steady point
    iq_m = linspace(0, 1.25*iq_ss, 200);
    id_m = id_ss*(iq_m/iq_ss).^2;
    fig = figure;
    hold on;
    plot(id_m, iq_m, '--', 'Color', palette('cat', 2), 'LineWidth', 1.5);
    plot(real(z), imag(z), '-', 'Color', palette('cat', 1), 'LineWidth', 1.2);
    plot(0, 0, 'o', 'Color', palette('cat', 3), ...
         'MarkerFaceColor', palette('cat', 3), 'MarkerSize', 5);
    plot(id_ss, iq_ss, 'p', 'Color', palette('cat', 4), ...
         'MarkerFaceColor', palette('cat', 4), 'MarkerSize', 11);
    text(id_ss + 3, iq_ss + 3, sprintf('(%.0f, %.0f) A', id_ss, iq_ss), ...
         'FontSize', 8);
    hold off;
    xlabel('i_d (A)'); ylabel('i_q (A)'); title('dq-axis current locus');
    legend({'MTPA trajectory', 'start-up transient', 'start (0, 0)', ...
            'steady-state point'}, 'Location', 'southwest', 'Box', 'off');
    grid on;
end
