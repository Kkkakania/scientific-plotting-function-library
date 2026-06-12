function fig = voltage_flicker()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    % amplitude-modulated 50 Hz carrier; 8.8 Hz is the most sensitive
    % flicker frequency per the IEC 61000-4-15 weighting peak
    f = 50; fm = 8.8; m = 0.08;
    t = linspace(0, 1, 6000);
    env = 1 + m * sin(2*pi*fm*t);
    v = env .* sin(2*pi*f*t);
    % 12 ten-minute short-term flicker severities; limit Pst = 1.0
    pst = max(0.65 + 0.18 * randn(1, 12), 0.2);
    pst(5) = 1.25; pst(6) = 1.42;        % arc-furnace heavy-melt intervals
    c0 = palette('cat',1); c1 = palette('cat',2);
    fig = figure('Position',[100 100 700 500]);
    subplot(2, 1, 1); hold on;
    plot(t, v, 'Color', c0, 'LineWidth', 0.4);
    henv = plot(t, env, 'Color', c1, 'LineWidth', 1.5);
    plot(t, -env, 'Color', c1, 'LineWidth', 1.5);
    xlabel('time (s)'); ylabel('voltage (pu)');
    title('Voltage flicker');
    legend(henv, {'modulation envelope'}, 'Location', 'northeast');
    grid on;
    subplot(2, 1, 2); hold on;
    idx = 1:numel(pst);
    hb = bar(idx, pst, 0.6, 'FaceColor', 'flat', 'EdgeColor', 'none');
    for k = idx
        if pst(k) > 1.0, hb.CData(k, :) = c1; else, hb.CData(k, :) = c0; end
    end
    hlim = plot([0.3 numel(pst)+0.7], [1.0 1.0], '--', 'Color', c1, ...
                'LineWidth', 1.2);
    set(gca, 'XTick', idx);
    xlabel('10-min interval'); ylabel('Pst');
    title('Short-term flicker severity');
    legend(hlim, {'Pst limit = 1.0'}, 'Location', 'northwest');
    set(gca, 'XGrid', 'off', 'YGrid', 'on');
end
