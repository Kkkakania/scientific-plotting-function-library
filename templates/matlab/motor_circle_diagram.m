function fig = motor_circle_diagram()
%MOTOR_CIRCLE_DIAGRAM 感应电机 Heyland 圆图（电流轨迹、功率/转矩线、效率刻度）
%   单相等效电路: Zm = jXm//Rc, Z2 = R2/s + jX2,
%   I1 = V/(R1 + jX1 + Zm*Z2/(Zm+Z2))；I1(s) 轨迹为圆。
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    v = 230; r1 = 0.5; x1 = 1.5; r2 = 0.6; x2 = 1.5; xm = 40; rc = 800;
    s_rated = 0.04;
    zm = 1j*xm*rc/(rc + 1j*xm);
    i1f = @(s) v ./ (r1 + 1j*x1 + zm*(r2./s + 1j*x2)./(zm + r2./s + 1j*x2));
    i2f = @(s) i1f(s) .* zm ./ (zm + r2./s + 1j*x2);
    % 轨迹（0<s<=1）
    s_arc = [logspace(-4, -1, 200) linspace(0.1, 1.0, 200)];
    iarc = i1f(s_arc);
    o = i1f(1e-4); sc = i1f(1.0); tt = i1f(1e6); a = i1f(s_rated);
    % 复平面坐标: x = -Im(I1), y = Re(I1)
    z = @(i) -imag(i) + 1j*real(i);
    zo = z(o); zs = z(sc); zt = z(tt); za = z(a);
    % 三点定圆
    w = (zt - zo)/(zs - zo);
    zc = zo + (zs - zo)*(w - abs(w)^2)/(2j*imag(w));
    rad = abs(zo - zc);
    th = linspace(0, 2*pi, 300);
    fig = figure('Position', [100 80 640 480]); hold on;
    plot(real(zc) + rad*cos(th), imag(zc) + rad*sin(th), '--', ...
         'Color', [0.75 0.75 0.75], 'LineWidth', 0.8, 'HandleVisibility', 'off');
    plot(-imag(iarc), real(iarc), 'Color', palette('cat',1), 'LineWidth', 1.8, ...
         'DisplayName', 'Current locus (0<s<1)');
    plot(real([zo zs]), imag([zo zs]), 'Color', palette('cat',2), ...
         'LineWidth', 1.2, 'DisplayName', 'Output line');
    plot(real([zo zt]), imag([zo zt]), 'Color', palette('cat',3), ...
         'LineWidth', 1.2, 'DisplayName', 'Torque line');
    % 额定点垂线与损耗分段
    kout = (imag(zs) - imag(zo))/(real(zs) - real(zo));
    ktq  = (imag(zt) - imag(zo))/(real(zt) - real(zo));
    xa = real(za); ya = imag(za);
    y_out = imag(zo) + kout*(xa - real(zo));
    y_tq  = imag(zo) + ktq *(xa - real(zo));
    plot([xa xa], [0 ya], ':', 'Color', [0.4 0.4 0.4], 'HandleVisibility', 'off');
    text(xa + 0.3, (y_out + ya)/2, 'P_{out}', 'FontSize', 7);
    text(xa + 0.3, (y_tq + y_out)/2, 'P_{cu,rotor}', 'FontSize', 7);
    text(xa + 0.3, (imag(zo) + y_tq)/2, 'P_{cu,stator}', 'FontSize', 7);
    text(xa + 0.3, imag(zo)/2, 'P_{fixed}', 'FontSize', 7);
    % 效率刻度
    s_tick = [0.01 0.02 0.05 0.10 0.30];
    it = i1f(s_tick); i2t = i2f(s_tick);
    eta = (3*abs(i2t).^2*r2.*(1 - s_tick)./s_tick) ./ (3*v*real(it));
    plot(-imag(it), real(it), '_', 'Color', palette('cat',4), 'MarkerSize', 7, ...
         'HandleVisibility', 'off');
    for k = 1:numel(s_tick)
        text(-imag(it(k)) - 0.4, real(it(k)) + 0.6, ...
             sprintf('\\eta=%.0f%%', eta(k)*100), 'FontSize', 7, ...
             'Color', palette('cat',4), 'HorizontalAlignment', 'right');
    end
    % 关键点
    pts = [zo zs za]; labs = {'O (no load)', 'S (s=1)', sprintf('A (s=%g)', s_rated)};
    dys = [-0.8 0.5 0.6];
    for k = 1:3
        plot(real(pts(k)), imag(pts(k)), 'o', 'Color', palette('cat',1), ...
             'MarkerSize', 5, 'MarkerFaceColor', palette('cat',1), ...
             'HandleVisibility', 'off');
        text(real(pts(k)) + 0.3, imag(pts(k)) + dys(k), labs{k}, 'FontSize', 8);
    end
    xlabel('reactive current (A)'); ylabel('active current (A)');
    title('Induction motor circle diagram (Heyland)');
    axis equal; xlim([-5 max(real(zc)+rad)*1.15]); ylim([-5 max(imag(zc)+rad)*1.3]);
    legend('Location', 'northeast', 'FontSize', 7); grid on;
end
