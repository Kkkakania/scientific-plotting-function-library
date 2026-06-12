function fig = pq_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % each index normalized to its standard limit so that 1.0 = limit:
    % THD/5%, VUF/2%, Pst/1.0, freq dev/0.2 Hz, sag count/planning level
    cats = {'THD', 'unbalance', 'flicker Pst', 'freq deviation', 'sag rate'};
    series = [0.45 0.30 0.40 0.25 0.35;    % residential feeder
              0.95 0.70 1.25 0.40 1.10;    % industrial feeder
              0.55 0.45 0.60 0.35 0.50];   % after APF mitigation
    names = {'residential', 'industrial', 'after mitigation'};
    n = numel(cats);
    ang = linspace(0, 2*pi, n+1);
    fig = figure('Position',[100 100 600 500]);
    pax = polaraxes; hold(pax, 'on');
    % unity polygon = compliance limit
    polarplot(pax, ang, ones(1, n+1), '--', 'Color', [0.4 0.4 0.4], ...
              'LineWidth', 1.2);
    for k = 1:size(series, 1)
        v = [series(k,:) series(k,1)];
        polarplot(pax, ang, v, 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    pax.ThetaTick = ang(1:end-1) * 180/pi;
    pax.ThetaTickLabel = cats;
    pax.RLim = [0 1.4]; pax.RTick = [0.5 1.0];
    pax.FontSize = 8;
    title('Power quality radar');
    legend([{'standard limit'} names], 'Location', 'southoutside', 'FontSize', 7);
end
