function fig = battery_soc_schedule()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    h = 0:23;
    P = [1.2 1.4 1.5 1.5 1.3 0.6 -0.4 -1.2 -0.8 -0.2 0.4 0.8 ...
         1.0 0.6 0.2 -0.3 -1.0 -1.6 -1.8 -1.4 -0.6 0.2 0.8 1.1];
    soc = 35 + cumsum(-P)*100/(2*24/1.5); soc = min(max(soc, 10), 95);
    fig = figure;
    yyaxis left; hold on;
    bc = bar(h(P>=0), P(P>=0), 0.8, 'FaceColor', palette('cat',1), 'DisplayName', 'charging');
    bd = bar(h(P<0), P(P<0), 0.8, 'FaceColor', palette('cat',2), 'DisplayName', 'discharging');
    yline(0, 'Color', [0.3 0.3 0.3], 'LineWidth', 0.8, 'HandleVisibility', 'off');
    ylabel('power (MW)  +charge / -discharge');
    set(gca, 'YColor', 'k');
    yyaxis right;
    ps = plot(h, soc, 'o-', 'Color', palette('cat',3), 'MarkerSize', 4, 'DisplayName', 'SOC');
    ylabel('SOC (%)'); ylim([0 100]); set(gca, 'YColor', palette('cat',3));
    xlabel('hour'); title('BESS dispatch and state of charge');
    legend([bc bd ps], 'Location', 'northwest', 'FontSize', 7); grid on;
end
