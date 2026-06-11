function fig = thermal_transient()
    % Foster 3 阶 RC 热网络: Tj(t) = Ta + P * sum_i R_i*(1 - exp(-t/tau_i))
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    p_levels = [100 200 300];                                % W 阶跃功率
    ta = 40; tj_max = 150;                                   % 环境温度 / 限值 (C)
    r = [0.05 0.18 0.32];                                    % K/W (芯片/基板/散热器)
    tau = [2e-3 8e-2 2.0];                                   % s
    t = logspace(-4, 1.3, 400)';
    zth = sum(r .* (1 - exp(-t ./ tau)), 2);                 % 阶跃热阻抗
    fig = figure; hold on;
    h = gobjects(1, numel(p_levels));
    for i = 1:numel(p_levels)
        h(i) = semilogx(t, ta + p_levels(i)*zth, 'Color', palette('cat', i), ...
                        'DisplayName', sprintf('P = %g W', p_levels(i)));
    end
    yline(tj_max, '--', sprintf('Tj,max = %g {\\circ}C', tj_max), ...
          'Color', palette('cat', 2), 'LineWidth', 1.2, ...
          'LabelHorizontalAlignment', 'left', 'FontSize', 8);
    set(gca, 'XScale', 'log'); xlim([t(1) t(end)]);
    ylim([ta-5, ta + max(p_levels)*zth(end) + 25]);
    xlabel('time (s)'); ylabel('junction temperature (\circC)');
    title('Junction temperature step response (Foster network)');
    legend(h, 'Location', 'northwest', 'Box', 'off'); grid on;
end
