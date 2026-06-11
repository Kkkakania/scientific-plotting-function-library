function fig = battery_degradation()
    % 容量衰减经验模型: fade(%) = k * DOD^1.5 * sqrt(N)
    % sqrt(N) 对应 SEI 膜扩散控制生长, DOD^1.5 反映深放电应力加速; k=0.37
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    dods = [0.6 0.8 1.0]; k = 0.37; eol = 80;
    n = linspace(0, 6000, 300);
    fig = figure; hold on;
    h = gobjects(1, numel(dods));
    for i = 1:numel(dods)
        q = 100 - k * dods(i)^1.5 * sqrt(n);
        h(i) = plot(n, q, 'Color', palette('cat', i), ...
                    'DisplayName', sprintf('DOD = %.0f%%', dods(i)*100));
        n_meas = 250:500:6000;                                % 每 500 循环抽检
        q_meas = 100 - k * dods(i)^1.5 * sqrt(n_meas) + 0.45*randn(size(n_meas));
        plot(n_meas, q_meas, 'o', 'MarkerSize', 4, 'MarkerFaceColor', 'w', ...
             'MarkerEdgeColor', palette('cat', i), 'LineWidth', 1.0);
    end
    yline(eol, '--', sprintf('EOL = %.0f%%', eol), 'Color', palette('cat', 8), ...
          'LineWidth', 1.2, 'LabelHorizontalAlignment', 'left', 'FontSize', 8);
    xlim([0 6000]); ylim([62 102]);
    xlabel('cycle number'); ylabel('capacity retention (%)');
    title('Battery capacity fade vs cycle number');
    legend(h, 'Location', 'southwest', 'Box', 'off');
    grid on;
end
