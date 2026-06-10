function fig = converter_efficiency_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    n = linspace(0, 6000, 200); T = linspace(0, 250, 200);
    [N, TT] = meshgrid(n, T);
    env = 250*min(1, 2500./max(N, 1));
    eta = 0.97 - 0.10*((N/6000 - 0.55).^2 + (TT/250 - 0.45).^2) ...
          - 0.05*exp(-N/600) - 0.03*exp(-TT/25);
    eta = eta*100; eta(TT > env) = NaN;
    fig = figure;
    contourf(N, TT, eta, linspace(78, 96, 19), 'LineStyle', 'none'); hold on;
    [cs, hh] = contour(N, TT, eta, [80 85 88 90 92 93 94 95], 'w', 'LineWidth', 0.7);
    clabel(cs, hh, 'FontSize', 7, 'Color', 'w');
    plot(n, 250*min(1, 2500./max(n, 1)), 'k', 'LineWidth', 1.4);
    colormap(sci_palettes('glacier'));
    cb = colorbar; cb.Label.String = 'efficiency (%)';
    xlabel('speed (rpm)'); ylabel('torque (N·m)');
    title('Inverter-motor efficiency map');
end
