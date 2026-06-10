function fig = economic_dispatch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    P = linspace(50, 400, 300);
    units = [0.004 5.5 120; 0.006 4.8 90; 0.009 4.0 60];
    lam = 7.2;
    fig = figure;
    subplot(1,2,1); hold on;
    for i = 1:3
        plot(P, units(i,1)*P.^2 + units(i,2)*P + units(i,3), ...
             'Color', palette('cat', i), 'DisplayName', sprintf('Unit %d', i));
    end
    xlabel('P (MW)'); ylabel('cost ($/h)'); title('cost curves'); legend('Location','northwest'); grid on;
    subplot(1,2,2); hold on;
    for i = 1:3
        plot(P, 2*units(i,1)*P + units(i,2), 'Color', palette('cat', i), ...
             'DisplayName', sprintf('Unit %d', i));
        Popt = (lam - units(i,2))/(2*units(i,1));
        plot(Popt, lam, 'o', 'Color', palette('cat', i), 'MarkerSize', 5, 'HandleVisibility', 'off');
    end
    yline(lam, '--', 'system \lambda', 'Color', [0.3 0.3 0.3], 'HandleVisibility', 'off');
    xlabel('P (MW)'); ylabel('incremental cost ($/MWh)');
    title('equal-\lambda dispatch'); legend('Location','northwest'); grid on;
end
