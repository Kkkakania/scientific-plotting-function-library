function fig = power_triangle(P, Q)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    if nargin < 1, P = 8; end
    if nargin < 2, Q = 6; end
    S = hypot(P, Q); phi = atan2(Q, P);
    fig = figure('Position',[100 100 600 500]); hold on;
    annotation_arrow([0 0], [P 0], palette('cat',1));
    annotation_arrow([P 0], [P Q], palette('cat',2));
    annotation_arrow([0 0], [P Q], palette('cat',3));
    text(P/2, -0.4, sprintf('P = %d kW', P), 'Color', palette('cat',1), 'HorizontalAlignment','center');
    text(P+0.3, Q/2, sprintf('Q = %d kVAr', Q), 'Color', palette('cat',2));
    text(P/2-0.3, Q/2+0.4, sprintf('S = %.2f kVA', S), 'Color', palette('cat',3));
    th = linspace(0, phi, 30);
    plot(cos(th), sin(th), 'k');
    text(1.5*cos(phi/2), 1.5*sin(phi/2), sprintf('\\phi = %.1f°', rad2deg(phi)));
    xlim([-1 P+3]); ylim([-1.5 Q+2]); axis equal;
    xlabel('P'); ylabel('Q'); title('Power triangle'); grid on;
end

function annotation_arrow(p1, p2, c)
    quiver(p1(1), p1(2), p2(1)-p1(1), p2(2)-p1(2), 0, ...
           'Color', c, 'LineWidth', 2, 'MaxHeadSize', 0.3);
end
