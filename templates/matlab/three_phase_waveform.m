function fig = three_phase_waveform()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = 50; Um = 311; t = linspace(0, 0.04, 1000);
    ua = Um*sin(2*pi*f*t);
    ub = Um*sin(2*pi*f*t - 2*pi/3);
    uc = Um*sin(2*pi*f*t + 2*pi/3);
    fig = figure('Position',[100 100 1000 450]);
    subplot(1, 2, 1);
    plot(t*1000, ua, 'Color', palette('cat',1)); hold on;
    plot(t*1000, ub, 'Color', palette('cat',2));
    plot(t*1000, uc, 'Color', palette('cat',3));
    yline(0, 'Color', [0.6 0.6 0.6]);
    xlabel('t (ms)'); ylabel('voltage (V)'); title('Time domain');
    legend({'Ua','Ub','Uc'}); grid on;
    subplot(1, 2, 2);
    pax = polaraxes; hold(pax, 'on');
    ang = [0 -2*pi/3 2*pi/3]; lab = {'Ua','Ub','Uc'};
    for k = 1:3
        polarplot([0 ang(k)], [0 Um], 'Color', palette('cat',k), 'LineWidth', 2);
        text(ang(k), Um*1.1, lab{k}, 'Color', palette('cat',k), 'HorizontalAlignment','center');
    end
    title('Phasor');
    sgtitle('Three-phase');
end
