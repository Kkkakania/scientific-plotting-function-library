function fig = unbalance_phasor()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    a = exp(2i*pi/3);
    % unbalanced three-phase set, single-phase load on phase B
    vabc = [1.00 * exp(1i * deg2rad(0)); ...
            0.78 * exp(-1i * deg2rad(118)); ...
            0.95 * exp(1i * deg2rad(123))];
    % Fortescue transform
    F = [1 1 1; 1 a a^2; 1 a^2 a] / 3;
    vseq = F * vabc;
    v0 = vseq(1); v1 = vseq(2); v2 = vseq(3);
    % each sequence is itself a balanced three-phase set
    names = {'Positive seq', 'Negative seq', 'Zero seq'};
    sets = {[v1, a^2*v1, a*v1], [v2, a*v2, a^2*v2], [v0, v0, v0]};
    vuf = abs(v2) / abs(v1) * 100;
    labs = {'A', 'B', 'C'};
    fig = figure('Position',[100 100 800 320]);
    for k = 1:3
        ax = subplot(1, 3, k);
        pos = get(ax, 'Position'); delete(ax);
        pax = polaraxes('Position', pos); hold(pax, 'on');
        comp = sets{k};
        for i = 1:3
            v = comp(i); c = palette('cat',i);
            polarplot(pax, [0 angle(v)], [0 abs(v)], 'Color', c, ...
                      'LineWidth', 1.5);
            polarplot(pax, angle(v), abs(v), 'o', 'Color', c, ...
                      'MarkerFaceColor', c, 'MarkerSize', 3);
            text(pax, angle(v), abs(v)*1.18 + 0.06, labs{i}, 'Color', c, ...
                 'FontSize', 8, 'HorizontalAlignment', 'center');
        end
        pax.RLim = [0 1.15];
        pax.RTick = [0.5 1.0]; pax.RTickLabel = {};
        pax.ThetaTick = [0 90 180 270];
        pax.FontSize = 7;
        title(pax, sprintf('%s  |V| = %.3f pu', names{k}, abs(comp(1))), ...
              'FontSize', 8);
    end
    sgtitle(sprintf('Symmetrical component decomposition  (VUF = %.1f%%)', ...
                    vuf), 'FontSize', 10);
end
