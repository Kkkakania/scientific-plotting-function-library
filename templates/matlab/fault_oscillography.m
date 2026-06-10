function fig = fault_oscillography()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 0.2, 4000); w = 2*pi*50; t_fault = 0.04; tau = 0.045;
    phases = 'abc';
    fig = figure;
    for i = 1:3
        th = -2*pi*(i-1)/3;
        pre = sin(w*t + th);
        dc = -6*sin(th + w*t_fault)*exp(-(t - t_fault)/tau);
        post = 6*sin(w*t + th) + dc;
        ia = pre; ia(t >= t_fault) = post(t >= t_fault);
        subplot(3, 1, i);
        plot(t*1000, ia, 'Color', palette('cat', i), 'LineWidth', 1.2);
        xline(t_fault*1000, '--', 'Color', [0.4 0.4 0.4]);
        ylabel(sprintf('i_%c (p.u.)', phases(i))); grid on;
        if i == 1, title('Three-phase fault oscillography'); end
    end
    xlabel('time (ms)');
end
