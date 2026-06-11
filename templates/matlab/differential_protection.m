function fig = differential_protection()
%DIFFERENTIAL_PROTECTION 差动保护比率制动特性（动作/制动区 + 故障样本散点）
%   模型: Id = |I1+I2|, Ir = |I1-I2|/2；两折线比率制动特性。
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    id_min = 0.3; ir1 = 0.5; k1 = 0.5; ir2 = 3.0; k2 = 0.7;
    charf = @(ir) (ir <= ir1).*id_min ...
        + (ir > ir1 & ir <= ir2).*(id_min + k1*(ir - ir1)) ...
        + (ir > ir2).*(id_min + k1*(ir2 - ir1) + k2*(ir - ir2));
    ir = linspace(0, 6, 400); idop = charf(ir);
    fig = figure; hold on;
    fill([ir fliplr(ir)], [idop 6*ones(1, numel(ir))], palette('cat',2), ...
         'FaceAlpha', 0.15, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    fill([ir fliplr(ir)], [zeros(1, numel(ir)) fliplr(idop)], palette('cat',1), ...
         'FaceAlpha', 0.12, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    plot(ir, idop, 'Color', [0.25 0.25 0.25], 'LineWidth', 1.8, ...
         'DisplayName', 'operating characteristic');
    text(1.0, 4.6, 'OPERATE', 'Color', palette('cat',2), 'FontWeight', 'bold');
    text(4.0, 0.8, 'RESTRAIN', 'Color', palette('cat',1), 'FontWeight', 'bold');
    % 内部故障样本（差流 ≈ 2*Ir）
    ir_int = 0.3 + 2.3*rand(1, 28);
    id_int = ir_int*2 .* (0.85 + 0.15*rand(1, 28)) + 0.08*randn(1, 28);
    % 外部故障/正常负荷（CT 误差差流 3~16%）
    ir_ext = 0.3 + 5.3*rand(1, 34);
    id_ext = ir_ext .* (0.03 + 0.13*rand(1, 34)) + abs(0.04*randn(1, 34));
    scatter(ir_int, id_int, 26, palette('cat',2), '^', 'filled', ...
            'MarkerEdgeColor', 'w', 'LineWidth', 0.5, 'DisplayName', 'internal faults');
    scatter(ir_ext, id_ext, 24, palette('cat',1), 'o', 'filled', ...
            'MarkerEdgeColor', 'w', 'LineWidth', 0.5, 'DisplayName', 'external faults / load');
    % 拐点
    knees = [ir1 ir2]; labs = {'knee 1', 'knee 2'};
    for i = 1:2
        y_ = charf(knees(i));
        plot(knees(i), y_, 's', 'Color', [0.25 0.25 0.25], 'MarkerSize', 4, ...
             'HandleVisibility', 'off');
        text(knees(i) + 0.12, y_ - 0.22, labs{i}, 'FontSize', 7);
    end
    xlabel('restraint current I_r (p.u.)'); ylabel('differential current I_d (p.u.)');
    title('Percentage differential protection characteristic');
    xlim([0 6]); ylim([0 6]);
    legend('Location', 'northwest', 'FontSize', 8); grid on;
end
