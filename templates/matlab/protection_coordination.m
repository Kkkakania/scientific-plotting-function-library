function fig = protection_coordination()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % downstream relay R1 (feeder) and upstream relay R2 (transformer)
    [i1, t1] = staged_curve(200, 0.05, 800, 0.30, 2000, 0.05);
    [i2, t2] = staged_curve(400, 0.10, 1200, 0.62, 4000, 0.37);
    fig = figure;
    loglog(i1, t1, '-', 'Color', palette('cat', 1), 'LineWidth', 1.5);
    hold on;
    loglog(i2, t2, '-', 'Color', palette('cat', 2), 'LineWidth', 1.5);
    % coordination margin at a common fault current
    i_f = 1500;
    ta = interp1(i1, t1, i_f); tb = interp1(i2, t2, i_f);
    cm = palette('cat', 4);
    plot([i_f i_f], [ta tb], '-', 'Color', cm, 'LineWidth', 1.2, ...
         'Marker', 'v', 'MarkerFaceColor', cm, 'MarkerSize', 4, ...
         'HandleVisibility', 'off');
    plot([i_f i_f], [0.02 20], ':', 'Color', cm, 'LineWidth', 0.8, ...
         'HandleVisibility', 'off');
    text(i_f*1.12, sqrt(ta*tb), ...
         sprintf('\\DeltaT = %.2f s \\geq 0.3 s', tb - ta), ...
         'Color', cm, 'FontSize', 8);
    hold off;
    xlabel('fault current (A)'); ylabel('operating time (s)');
    title('Overcurrent protection coordination');
    xlim([150 20000]); ylim([0.02 20]);
    legend({'R1 downstream (3-stage)', 'R2 upstream (3-stage)'}, ...
           'Location', 'northeast', 'Box', 'off');
    grid on; set(gca, 'XMinorGrid', 'on', 'YMinorGrid', 'on');
end

function [i, t] = staged_curve(ip3, tms, ip2, t2, ip1, t1)
    % 3-stage: IEC SI inverse-time -> definite-time -> instantaneous
    i = logspace(log10(ip3*1.05), log10(20000), 600);
    i = sort([i, ip2*(1 - 1e-9), ip2, ip1*(1 - 1e-9), ip1]);
    t = tms*0.14./((i/ip3).^0.02 - 1);
    t(i >= ip2) = min(t(i >= ip2), t2);
    t(i >= ip1) = t1;
end
