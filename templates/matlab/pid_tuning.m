function fig = pid_tuning()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 15, 1000);
    fig = figure; hold on;
    cfgs = {[2 0 0],   'P';
            [2 1 0],   'PI';
            [4 2 0.2], 'PID(4,2,0.2)';
            [8 4 0.5], 'PID(8,4,0.5)'};
    for i = 1:size(cfgs, 1)
        Kp = cfgs{i,1}(1); Ki = cfgs{i,1}(2); Kd = cfgs{i,1}(3);
        cn = [Kd Kp Ki]; cd = [1 0];
        pn = 1; pd = [1 1 1];
        on = conv(cn, pn); od = conv(cd, pd);
        cl_den = od;
        n_on = numel(on); n_od = numel(od);
        cl_den(end-n_on+1:end) = cl_den(end-n_on+1:end) + on;
        sys = tf(on, cl_den);
        y = lsim(sys, ones(size(t)), t);
        plot(t, y, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    yline(1, '--', 'Color', [0.5 0.5 0.5]);
    xlabel('t'); ylabel('y(t)'); title('PID tuning step response');
    legend(cfgs(:, 2)); grid on;
end
