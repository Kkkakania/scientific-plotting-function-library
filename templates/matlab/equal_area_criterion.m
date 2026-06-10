function fig = equal_area_criterion()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    Pm = 0.8; d = linspace(0, pi, 400);
    d0 = asin(Pm/1.8); dc = 1.05; dmax = pi - asin(Pm/1.3);
    fig = figure; hold on;
    plot(rad2deg(d), 1.8*sin(d), 'Color', palette('cat',1), 'DisplayName', 'pre-fault');
    plot(rad2deg(d), 0.4*sin(d), 'Color', palette('cat',2), 'DisplayName', 'during fault');
    plot(rad2deg(d), 1.3*sin(d), 'Color', palette('cat',3), 'DisplayName', 'post-fault');
    yline(Pm, '--', 'Color', [0.3 0.3 0.3], 'HandleVisibility', 'off');
    m1 = d >= d0 & d <= dc;
    fill([rad2deg(d(m1)) fliplr(rad2deg(d(m1)))], [0.4*sin(d(m1)) Pm*ones(1,sum(m1))], ...
         palette('cat',2), 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    m2 = d >= dc & d <= dmax & 1.3*sin(d) >= Pm;
    fill([rad2deg(d(m2)) fliplr(rad2deg(d(m2)))], [Pm*ones(1,sum(m2)) fliplr(1.3*sin(d(m2)))], ...
         palette('cat',3), 'FaceAlpha', 0.3, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    text(rad2deg((d0+dc)/2), Pm-0.12, 'A1', 'HorizontalAlignment', 'center');
    text(rad2deg((dc+dmax)/2), Pm+0.14, 'A2', 'HorizontalAlignment', 'center');
    xlabel('rotor angle \delta (deg)'); ylabel('power (p.u.)');
    title('Equal-area criterion'); legend; grid on; ylim([0 2]);
end
