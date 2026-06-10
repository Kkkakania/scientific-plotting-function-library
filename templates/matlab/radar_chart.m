function fig = radar_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    cats = {'speed','power','efficiency','cost','reliability','noise'};
    n = numel(cats); V = 0.3 + 0.7*rand(3, n);
    ang = linspace(0, 2*pi, n+1);
    fig = figure;
    pax = polaraxes; hold(pax, 'on');
    for k = 1:3
        v = [V(k,:) V(k,1)];
        polarplot(pax, ang, v, 'Color', palette('cat',k), 'LineWidth', 1.5);
        polarplot(pax, ang, v, 'o', 'Color', palette('cat',k), 'MarkerFaceColor', palette('cat',k));
    end
    pax.ThetaTick = ang(1:end-1) * 180/pi;
    pax.ThetaTickLabel = cats;
    title('Radar');
    legend({'A','','B','','C',''}, 'Location','southoutside');
end
