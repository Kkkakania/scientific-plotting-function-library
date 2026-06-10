function fig = duck_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 24, 480);
    load_curve = 20 + 6*exp(-0.5*((t - 9)/2.6).^2) + 9*exp(-0.5*((t - 19.5)/2.0).^2);
    pv_shape = exp(-0.5*((t - 12.5)/2.7).^2) .* (abs(t - 12.5) < 7);
    years = 2018:2:2026;
    cmap = sci_palettes('blues', numel(years) + 3);
    fig = figure; hold on;
    for i = 1:numel(years)
        net = load_curve - 2.2*(i-1)*pv_shape;
        plot(t, net, 'Color', cmap(i+2, :), 'DisplayName', num2str(years(i)));
    end
    annotation('textarrow', [0.55 0.67], [0.42 0.52], 'String', 'growing ramp', 'FontSize', 8);
    xlabel('hour of day'); ylabel('net load (GW)');
    title('Duck curve: net load vs PV penetration');
    xlim([0 24]); legend('Location', 'southwest', 'FontSize', 7); grid on;
end
