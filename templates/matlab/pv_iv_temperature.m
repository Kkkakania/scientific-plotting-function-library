function fig = pv_iv_temperature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    V = linspace(0, 48, 400); temps = [0 25 50 75];
    cmap = sci_palettes('oranges', numel(temps) + 3);
    fig = figure;
    subplot(1,2,1); hold on;
    subplot(1,2,2); hold on;
    for i = 1:numel(temps)
        T = temps(i);
        Voc = 44 - 0.16*(T - 25); Isc = 9.0*(1 + 0.0005*(T - 25));
        I = max(Isc*(1 - exp((V - Voc)/2.2)), 0);
        c = cmap(i+2, :);
        subplot(1,2,1);
        plot(V, I, 'Color', c, 'DisplayName', sprintf('%d °C', T));
        subplot(1,2,2);
        plot(V, V.*I, 'Color', c, 'DisplayName', sprintf('%d °C', T));
        [Pm, kk] = max(V.*I);
        plot(V(kk), Pm, 'o', 'Color', c, 'MarkerSize', 4, 'HandleVisibility', 'off');
    end
    subplot(1,2,1); xlabel('voltage (V)'); ylabel('current (A)'); title('I-V');
    legend('FontSize', 7, 'Location', 'southwest'); grid on;
    subplot(1,2,2); xlabel('voltage (V)'); ylabel('power (W)'); title('P-V with MPP');
    legend('FontSize', 7, 'Location', 'northwest'); grid on;
end
