function fig = pq_injection_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(42);
    % IEEE-14 style demo data: 14 buses x 24 hours, generators > 0, loads < 0
    hours = 0:23;
    profile = 0.7 + 0.3*sin((hours - 6)/24*2*pi);
    gen_buses = [1 2 3 6 8];
    p_base = -0.6 + 0.45*rand(14, 1);                  % loads draw P (<0)
    p_base(gen_buses) = [2.3; 0.4; 0; 0; 0] + 0.2 + 0.7*rand(5, 1);
    q_base = 0.35*p_base + 0.05*randn(14, 1);
    P = p_base*profile + 0.03*randn(14, 24);
    Q = q_base*profile + 0.02*randn(14, 24);
    data = {P, Q};
    names = {'Active power P (p.u.)', 'Reactive power Q (p.u.)'};
    fig = figure('Position', [100 100 850 420]);
    for k = 1:2
        ax = subplot(1, 2, k);
        M = data{k};
        imagesc(ax, hours, 1:14, M);
        colormap(ax, palette('div'));
        vmax = max(abs(M(:)));
        caxis(ax, [-vmax vmax]);
        cb = colorbar(ax); ylabel(cb, 'injection (p.u.)');
        xlabel(ax, 'hour of day'); ylabel(ax, 'bus number');
        title(ax, names{k});
        set(ax, 'YTick', 1:14, 'XTick', 0:6:23, 'YDir', 'normal');
        grid(ax, 'on');
    end
    sgtitle('Bus P/Q injection profile (IEEE-14)');
end
