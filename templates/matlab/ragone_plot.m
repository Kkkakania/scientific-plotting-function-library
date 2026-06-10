function fig = ragone_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    techs = {180 300 0.25 0.45 'Li-ion'; 35 150 0.30 0.40 'Lead-acid';
             90 180 0.30 0.45 'NiMH'; 5 4000 0.45 0.50 'Supercapacitor';
             0.05 8000 0.50 0.40 'Electrolytic cap.'; 30 1200 0.35 0.40 'Flywheel';
             450 60 0.30 0.50 'Fuel cell'};
    fig = figure; hold on;
    tt = linspace(0, 2*pi, 60);
    for i = 1:size(techs, 1)
        cx = log10(techs{i,1}); cy = log10(techs{i,2});
        c = palette('cat', i);
        fill(cx + techs{i,3}*cos(tt), cy + techs{i,4}*sin(tt), c, ...
             'FaceAlpha', 0.4, 'EdgeColor', c, 'LineWidth', 1.2);
        text(cx, cy, techs{i,5}, 'HorizontalAlignment', 'center', 'FontSize', 7.5);
    end
    taus = [36 3600 36000]; labs = {'1 min', '1 h', '10 h'};
    for i = 1:3
        x = [-2 3.2];
        plot(x, x + log10(3600/taus(i)), ':', 'Color', [0.75 0.75 0.75], 'LineWidth', 0.9);
        text(2.45, 2.45 + log10(3600/taus(i)) + 0.1, labs{i}, 'FontSize', 7, ...
             'Color', [0.4 0.4 0.4], 'Rotation', 38);
    end
    xlim([-2 3.2]); ylim([0.5 4.3]);
    xticks(-2:3); xticklabels(arrayfun(@(v) sprintf('10^{%d}', v), -2:3, 'UniformOutput', false));
    yticks(1:4); yticklabels(arrayfun(@(v) sprintf('10^{%d}', v), 1:4, 'UniformOutput', false));
    xlabel('specific energy (Wh/kg)'); ylabel('specific power (W/kg)');
    title('Ragone plot of storage technologies'); grid on;
end
