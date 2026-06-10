function fig = swing_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    t = linspace(0, 3, 600); t_clear = 0.25;
    f0 = [1.2 1.6 0.9];
    fig = figure; hold on;
    for i = 1:3
        d0 = 35 + 12*(i-1);
        tt = max(t - t_clear, 0);
        d = d0 + 38*exp(-0.35*tt).*sin(2*pi*f0(i)*tt).*(t > t_clear);
        plot(t, d, 'Color', palette('cat', i), 'DisplayName', sprintf('Gen %d', i));
    end
    xline(t_clear, '--', 'fault cleared', 'Color', [0.4 0.4 0.4]);
    xlabel('time (s)'); ylabel('rotor angle (deg)'); title('Rotor angle swing curves');
    legend('Location', 'northeast'); grid on;
end
