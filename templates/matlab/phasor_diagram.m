function fig = phasor_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    v_mag = 1.0; i_mag = 0.8; phi = 30;          % current lags 30 deg
    v_ang = deg2rad([0 -120 120]);               % Va, Vb, Vc
    i_ang = v_ang - deg2rad(phi);
    names_v = {'V_a', 'V_b', 'V_c'}; names_i = {'I_a', 'I_b', 'I_c'};
    fig = figure;
    pax = polaraxes; hold(pax, 'on');
    for k = 1:3
        c = palette('cat', k);
        draw_arrow(pax, v_ang(k), v_mag, c, '-', 1.8);
        draw_arrow(pax, i_ang(k), i_mag, c, '--', 1.4);
        text(pax, v_ang(k), v_mag*1.18, sprintf('%s 1.00\\angle%.0f%c', ...
             names_v{k}, rad2deg(v_ang(k)), char(176)), ...
             'Color', c, 'FontSize', 8, 'HorizontalAlignment', 'center');
        text(pax, i_ang(k), i_mag*0.60, sprintf('%s 0.80\\angle%.0f%c', ...
             names_i{k}, rad2deg(i_ang(k)), char(176)), ...
             'Color', c, 'FontSize', 7, 'HorizontalAlignment', 'center');
    end
    pax.RLim = [0 v_mag*1.35]; pax.RTick = [0.5 1.0];
    pax.GridLineStyle = ':'; pax.GridAlpha = 0.5;
    title(pax, 'Three-phase phasor diagram (magnitude in p.u., current lags 30\circ)');
    hv = polarplot(pax, NaN, NaN, '-', 'Color', [0.3 0.3 0.3], 'LineWidth', 1.8);
    hi = polarplot(pax, NaN, NaN, '--', 'Color', [0.3 0.3 0.3], 'LineWidth', 1.4);
    legend(pax, [hv hi], {'voltage (solid)', 'current (lags 30\circ)'}, ...
           'Location', 'northeastoutside', 'Box', 'off');
end

function draw_arrow(pax, th, r, c, ls, lw)
    % shaft + manually drawn arrowhead (polarplot has no native arrows)
    polarplot(pax, [th th], [0 r], 'LineStyle', ls, 'Color', c, ...
              'LineWidth', lw, 'HandleVisibility', 'off');
    [x, y] = pol2cart(th, r);
    hl = 0.07*r;                                 % arrowhead length
    for da = [pi - 0.35, pi + 0.35]
        xe = x + hl*cos(th + da); ye = y + hl*sin(th + da);
        [the, re] = cart2pol(xe, ye);
        polarplot(pax, [th the], [r re], '-', 'Color', c, ...
                  'LineWidth', lw, 'HandleVisibility', 'off');
    end
end
