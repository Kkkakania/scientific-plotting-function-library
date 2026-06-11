function fig = switching_loss_breakdown()
    % 功率器件损耗分解: P_cond 与 fsw 无关, P_on/P_off/P_rr = E*fsw 线性增长
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fsw_khz = [5 10 20 50]; fsw = fsw_khz * 1e3;
    % 典型 1200 V IGBT @ 600 V, 50 A, Tj = 125 C
    vce_sat = 1.1; r_ce = 9e-3; i_avg = 25; i_rms = 35;
    e_on = 2.0e-3; e_off = 1.5e-3; e_rr = 0.9e-3;            % J/脉冲
    p_cond = (vce_sat*i_avg + r_ce*i_rms^2) * ones(size(fsw));
    P = [p_cond; e_on*fsw; e_off*fsw; e_rr*fsw]';            % 4 列堆叠
    fig = figure;
    hb = bar(1:numel(fsw), P, 0.55, 'stacked');
    for i = 1:4, hb(i).FaceColor = palette('cat', i); end
    tot = sum(P, 2);
    text(1:numel(fsw), tot + 4, compose('%.0f W', tot), ...
         'HorizontalAlignment', 'center', 'FontSize', 8);
    set(gca, 'XTick', 1:numel(fsw), 'XTickLabel', compose('%g', fsw_khz));
    xlabel('switching frequency (kHz)'); ylabel('loss per device (W)');
    title('Power device loss breakdown vs switching frequency');
    legend({'Conduction','Turn-on','Turn-off','Reverse recovery'}, ...
           'Location', 'northwest', 'Box', 'off');
    grid on;
end
