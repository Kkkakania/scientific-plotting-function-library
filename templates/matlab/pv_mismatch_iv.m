function fig = pv_mismatch_iv()
    % 光伏阵列失配 I-V: 3 并联支路, 每条 = 2 个带旁路二极管的子串(18 cell)串联
    % 子串单二极管模型 V = Ns*n*Vt*ln((Iph-I)/I0+1), I>Iph 时旁路钳位 -0.6 V
    % 遮挡: 支路1 无遮挡(8/8 A), 支路2 半串 50%(8/4 A), 支路3 半串 75%(8/2 A)
    % 遮挡子串被旁路 → 支路 I-V 台阶, 阵列 P-V 多峰
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    iph_pairs = [8 8; 8 4; 8 2];
    labels = {'String 1 (no shading)', 'String 2 (50% shaded half)', ...
              'String 3 (75% shaded half)'};
    % 电流网格在各 Iph 附近加密以解析二极管膝点
    i = sort([linspace(0, 8.05, 600), 2-logspace(-8,-0.3,80), ...
              4-logspace(-8,-0.3,80), 8-logspace(-8,-0.3,80)]);
    v_grid = linspace(0, 24, 800);
    i_array = zeros(size(v_grid));
    fig = figure; hold on;
    h = gobjects(1, 5);
    for k = 1:3
        v_str = substring_v(i, iph_pairs(k,1)) + substring_v(i, iph_pairs(k,2));
        m = v_str >= 0;                                       % 发电象限
        h(k) = plot(v_str(m), i(m), 'Color', palette('cat', k), 'LineWidth', 1.2);
        [v_u, iu] = unique(v_str(m));                         % 按电压插值并联相加
        i_m = i(m); i_m = i_m(iu);
        iq = interp1(v_u, i_m, v_grid, 'linear');
        iq(v_grid <= v_u(1)) = i_m(1);                        % V→0 处取 Isc
        iq(v_grid >= v_u(end)) = 0;                           % 超过 Voc 电流为 0
        i_array = i_array + iq;
    end
    h(4) = plot(v_grid, i_array, 'Color', palette('cat', 4), 'LineWidth', 2.0);
    yyaxis right;                                             % 阵列功率多峰
    p = v_grid .* i_array;
    h(5) = plot(v_grid, p, '--', 'Color', palette('cat', 8), 'LineWidth', 1.2);
    ylabel('array power (W)'); ylim([0, max(p)*1.30]);
    set(gca, 'YColor', palette('cat', 8));
    yyaxis left;
    xlim([0 24]); ylim([0 26]);
    xlabel('voltage (V)'); ylabel('current (A)');
    title('PV array I-V under partial shading');
    legend(h, [labels, {'Array (parallel)', 'Array power'}], ...
           'Location', 'northwest', 'Box', 'off', 'FontSize', 7);
    grid on;
end

function v = substring_v(i, iph)
    i0 = 7e-8; n_vt = 0.0334; ns = 18; v_bypass = -0.6;
    v = ns * n_vt * log(max((iph - i)/i0 + 1, 1e-12));
    v(i >= iph) = v_bypass;
end
