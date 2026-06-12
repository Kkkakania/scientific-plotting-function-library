function fig = harmonic_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    orders = 2:25;
    hours = linspace(0, 24, 97);              % 15-min resolution
    % characteristic 6-pulse orders dominate; magnitude follows the
    % industrial load profile (high 8h-18h), plus measurement noise
    base = 0.15*ones(1, numel(orders));
    ks = [3 5 7 11 13 17 19 23];
    av = [1.2 4.0 2.8 1.6 1.3 0.7 0.6 0.4];
    for j = 1:numel(ks)
        base(orders == ks(j)) = av(j);
    end
    load_prof = 0.35 + 0.65*exp(-((hours - 13)/4.2).^2);
    amp = base' * load_prof;
    amp = amp + 0.08*rand(size(amp));
    fig = figure('Position', [100 100 700 400]);
    imagesc(hours, orders, amp);
    set(gca, 'YDir', 'normal');
    colormap(palette('seq_blue'));
    cb = colorbar;
    ylabel(cb, 'amplitude (% of fundamental)');
    xlabel('time of day (h)'); ylabel('harmonic order');
    title('Harmonic amplitude vs time of day');
    set(gca, 'XTick', 0:4:24, 'YTick', [3 5 7 11 13 17 19 23]);
end
