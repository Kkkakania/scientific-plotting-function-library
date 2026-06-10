function fig = wind_power_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    v_in = 3; v_rated = 12; v_out = 25;
    v = linspace(0, 28, 400);
    P = zeros(size(v));
    m = v >= v_in & v < v_rated;
    P(m) = (v(m).^3 - v_in^3)/(v_rated^3 - v_in^3);
    P(v >= v_rated & v < v_out) = 1;
    vs = 0.5 + 26.5*rand(1, 220);
    Ps = interp1(v, P, vs) + 0.03*randn(1, 220);
    Ps = max(min(Ps + (vs > v_in)*0.02.*randn(1, 220), 1.08), 0);
    fig = figure; hold on;
    scatter(vs, Ps, 12, palette('cat',6), 'filled', 'MarkerFaceAlpha', 0.45, ...
            'DisplayName', 'SCADA data');
    plot(v, P, 'Color', palette('cat',2), 'LineWidth', 2, 'DisplayName', 'design curve');
    marks = [v_in v_rated v_out]; labs = {'cut-in', 'rated', 'cut-out'};
    for i = 1:3
        xline(marks(i), ':', labs{i}, 'Color', [0.55 0.55 0.55], 'HandleVisibility', 'off');
    end
    xlabel('wind speed (m/s)'); ylabel('power (p.u.)');
    title('Wind turbine power curve'); ylim([-0.04 1.18]);
    legend('Location', 'east'); grid on;
end
