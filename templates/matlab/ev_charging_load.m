function fig = ev_charging_load()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 24, 480);
    base = 55 + 14*exp(-0.5*((t - 10)/3.0).^2) + 20*exp(-0.5*((t - 19.5)/2.2).^2);
    ev_unc = 12*exp(-0.5*((t - 19)/1.6).^2) + 4*exp(-0.5*((t - 8.5)/1.2).^2);
    ev_smart = 12*exp(-0.5*((t - 2.5)/2.6).^2) + 4*exp(-0.5*((t - 13)/2.2).^2);
    fig = figure; hold on;
    plot(t, base, '--', 'Color', [0.45 0.45 0.45], 'LineWidth', 1.2, 'DisplayName', 'base load');
    plot(t, base + ev_unc, 'Color', palette('cat',2), 'DisplayName', 'uncontrolled charging');
    plot(t, base + ev_smart, 'Color', palette('cat',3), 'DisplayName', 'smart charging');
    fill([t fliplr(t)], [base fliplr(base + ev_unc)], palette('cat',2), ...
         'FaceAlpha', 0.18, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    fill([t fliplr(t)], [base fliplr(base + ev_smart)], palette('cat',3), ...
         'FaceAlpha', 0.18, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    xlabel('hour of day'); ylabel('load (MW)');
    title('EV charging load: uncontrolled vs smart');
    xlim([0 24]); legend('FontSize', 8); grid on;
end
