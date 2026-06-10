function fig = power_factor_locus()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    h = linspace(0, 24, 200);
    fig = figure;
    plot(h, 0.95 - 0.05*sin((h-12)*pi/12), 'Color', palette('cat',1)); hold on;
    plot(h, 0.75 + 0.15*sin((h-12)*pi/12), 'Color', palette('cat',2));
    plot(h, 0.85 + 0.08*cos((h-14)*pi/12), 'Color', palette('cat',3));
    yline(0.9, '--r', 'target \geq 0.9');
    xlabel('hour'); ylabel('power factor'); title('Power factor over day');
    legend({'residential','industrial','commercial'}); xticks(0:3:24); grid on;
end
