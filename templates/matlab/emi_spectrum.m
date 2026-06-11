function fig = emi_spectrum()
    % 传导 EMI 准峰值包络 vs CISPR 22 Class B 限值, 超标段红色高亮
    % 包络模型: 梯形开关波形频谱, f1=1/(pi*D*Tsw) 后 -20 dB/dec,
    % f2=1/(pi*tr) 后再 -20 dB/dec; 叠加两处寄生谐振 Q 峰与测量纹波
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    f = logspace(log10(150e3), log10(30e6), 600);
    fsw = 100e3; d = 0.4; tr = 60e-9;
    f1 = 1/(pi*d/fsw); f2 = 1/(pi*tr);
    base = 92;
    env = base - 20*log10(max(f/f1, 1)) - 20*log10(max(f/f2, 1));
    res1 = 9 ./ (1 + ((log10(f) - log10(0.4e6))/0.06).^2);
    res2 = 14 ./ (1 + ((log10(f) - log10(18e6))/0.05).^2);
    qp = env + res1 + res2 + 0.8*randn(size(f));
    % CISPR 22 Class B QP 限值: 66→56 dBuV (0.15-0.5 MHz, log 线性), 56, 60
    lim = zeros(size(f));
    seg1 = f < 0.5e6; seg2 = f >= 0.5e6 & f < 5e6; seg3 = f >= 5e6;
    lim(seg1) = 66 - 10*log10(f(seg1)/0.15e6)/log10(0.5/0.15);
    lim(seg2) = 56; lim(seg3) = 60;
    over = qp > lim;
    fig = figure; hold on;
    h1 = semilogx(f/1e6, qp, 'Color', palette('cat',1), 'LineWidth', 1.0);
    h2 = semilogx(f/1e6, lim, '--', 'Color', palette('cat',8), 'LineWidth', 1.4);
    qp_over = qp; qp_over(~over) = NaN;                       % 超标段
    h3 = semilogx(f/1e6, qp_over, 'Color', [0.75 0 0], 'LineWidth', 1.8);
    set(gca, 'XScale', 'log'); xlim([0.15 30]); ylim([20 100]);
    xlabel('frequency (MHz)'); ylabel('amplitude (dB\muV)');
    title('Conducted EMI spectrum vs CISPR 22 Class B');
    legend([h1 h2 h3], {'Quasi-peak envelope', 'CISPR 22 Class B (QP)', ...
           'Above limit'}, 'Location', 'northeast', 'Box', 'off');
    grid on;
end
