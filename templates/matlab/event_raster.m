function fig = event_raster()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(16);
    n_ch = 8; T = 60.0;
    rates = 0.3 + 1.7*rand(1, n_ch);          % events per second per channel
    fig = figure('Position', [100 100 700 400]); hold on;
    for ch = 1:n_ch
        n_ev = round(rates(ch)*T*2) + 10;
        gaps = -log(rand(1, n_ev)) / rates(ch);   % exponential inter-event gaps
        tt = cumsum(gaps); tt = tt(tt < T);
        m = numel(tt);
        y0 = (ch - 1) - 0.35; y1 = (ch - 1) + 0.35;
        xs = [tt; tt; nan(1, m)];
        ys = [repmat(y0, 1, m); repmat(y1, 1, m); nan(1, m)];
        plot(xs(:), ys(:), 'Color', palette('cat', ch), 'LineWidth', 1.0);
    end
    set(gca, 'YTick', 0:n_ch-1, ...
        'YTickLabel', arrayfun(@(c) sprintf('ch %d', c), 1:n_ch, 'UniformOutput', false));
    xlim([0 T]); ylim([-0.8 n_ch - 0.2]);
    xlabel('time (s)'); ylabel('channel'); title('Event raster');
    grid on; set(gca, 'YGrid', 'off');
end
