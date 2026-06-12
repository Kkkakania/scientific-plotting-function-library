function fig = itic_tolerance_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    % ITIC (2000) envelope vertices: duration (s) vs voltage (% of nominal).
    % Steps are encoded by nearly-coincident x pairs so interp stays monotonic.
    UP_D = [1e-3 3e-3 3.0003e-3 0.5 0.50005 10.0];
    UP_V = [200 200 140 140 120 120];
    LO_D = [1e-3 0.02 0.020002 0.5 0.50005 10.0];
    LO_V = [0 0 70 70 80 80];
    % synthetic monitored events: mostly sags, a few swells/impulses
    n = 60;
    dur = 10.^(-3 + 4*rand(1, n));
    mag = [10 + 100*rand(1, n - 15), 112 + 118*rand(1, 15)];
    mag = mag(randperm(n));
    d = logspace(-3, 1, 500);
    up = interp1(log10(UP_D), UP_V, log10(d));
    lo = interp1(log10(LO_D), LO_V, log10(d));
    fig = figure; hold on;
    % regions: above upper = prohibited, between = ride-through, below = no-damage
    fill([d fliplr(d)], [up 240*ones(1, numel(d))], palette('cat',2), ...
         'FaceAlpha', 0.10, 'EdgeColor', 'none');
    fill([d fliplr(d)], [lo fliplr(up)], palette('cat',3), ...
         'FaceAlpha', 0.10, 'EdgeColor', 'none');
    fill([d fliplr(d)], [zeros(1, numel(d)) fliplr(lo)], palette('cat',8), ...
         'FaceAlpha', 0.18, 'EdgeColor', 'none');
    hup = plot(d, up, 'Color', palette('cat',2), 'LineWidth', 1.5);
    hlo = plot(d, lo, 'Color', palette('cat',8), 'LineWidth', 1.5);
    hi_ev = mag > interp1(log10(UP_D), UP_V, log10(dur));
    lo_ev = mag < interp1(log10(LO_D), LO_V, log10(dur));
    ok = ~hi_ev & ~lo_ev;
    hok = scatter(dur(ok), mag(ok), 16, palette('cat',3), 'filled');
    hhi = scatter(dur(hi_ev), mag(hi_ev), 18, palette('cat',2), '^', 'filled');
    hlt = scatter(dur(lo_ev), mag(lo_ev), 18, palette('cat',8), 'v', 'filled');
    plot([1e-3 10], [100 100], '--', 'Color', [0.6 0.6 0.6], 'LineWidth', 0.6);
    set(gca, 'XScale', 'log');
    xlim([1e-3 10]); ylim([0 240]);
    xlabel('event duration (s)'); ylabel('voltage (% of nominal)');
    title('ITIC voltage tolerance curve');
    legend([hup hlo hok hhi hlt], ...
           {'upper limit', 'lower limit', 'ride-through', 'prohibited', ...
            'no-damage trip'}, 'Location', 'northeast', 'FontSize', 7);
    grid on;
end
