function fig = grid_frequency_response()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 30, 1200);
    Hs = [6 4 2]; labels = {'H = 6 s (high inertia)', 'H = 4 s', 'H = 2 s (low inertia)'};
    fig = figure; hold on;
    for i = 1:3
        H = Hs(i); wn = 0.45*sqrt(4/H); zeta = 0.5; wd = wn*sqrt(1 - zeta^2);
        df = -0.65*(4/H)^0.35*exp(-zeta*wn*t).*sin(wd*t)/(wd*4);
        f = 50 + df - 0.05*(1 - exp(-t/8));
        plot(t, f, 'Color', palette('cat', i), 'DisplayName', labels{i});
        [fmin, k] = min(f);
        plot(t(k), fmin, 'v', 'Color', palette('cat', i), 'MarkerSize', 5, 'HandleVisibility', 'off');
    end
    yline(49.8, '--', 'UFLS threshold', 'Color', [0.4 0.4 0.4], 'HandleVisibility', 'off');
    xlabel('time (s)'); ylabel('frequency (Hz)');
    title('Frequency response after generation loss');
    legend('Location', 'southeast'); grid on;
end
