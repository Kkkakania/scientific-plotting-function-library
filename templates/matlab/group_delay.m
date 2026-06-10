function fig = group_delay()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure;
    hold on;
    for i = 1:4
        order = i*2;
        [b, a] = butter(order, 0.3);
        [gd, w] = grpdelay(b, a, 512);
        plot(w/pi, gd, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('normalized frequency'); ylabel('group delay (samples)');
    title('Group delay');
    legend({'order 2','order 4','order 6','order 8'}); grid on;
end
