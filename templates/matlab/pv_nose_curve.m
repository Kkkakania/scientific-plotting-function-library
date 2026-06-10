function fig = pv_nose_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    E = 1.0; X = 0.5; tans = [-0.2 0 0.2];
    fig = figure; hold on;
    for i = 1:numel(tans)
        pf_tan = tans(i);
        P = linspace(0, 1.05/sqrt(X*(1+pf_tan^2)), 400);
        Q = pf_tan*P;
        disc = E^4/4 - X^2*P.^2 - X*Q*E^2;
        m = disc >= 0;
        Vh = sqrt(E^2/2 - X*Q(m) + sqrt(disc(m)));
        Vl = sqrt(max(E^2/2 - X*Q(m) - sqrt(disc(m)), 0));
        c = palette('cat', i);
        plot(P(m), Vh, 'Color', c, 'DisplayName', sprintf('tan\\phi = %+.1f', pf_tan));
        plot(P(m), Vl, '--', 'Color', c, 'LineWidth', 1, 'HandleVisibility', 'off');
        Pm = P(m); plot(Pm(end), Vh(end), 'o', 'Color', c, 'MarkerSize', 4, 'HandleVisibility', 'off');
    end
    xlabel('P (p.u.)'); ylabel('V (p.u.)'); title('P-V nose curves');
    legend('Location', 'southwest'); grid on;
end
