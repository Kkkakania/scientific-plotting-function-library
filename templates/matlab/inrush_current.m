function fig = inrush_current()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = 50; fs = 5000; t = 0:1/fs:0.4;
    env = 8*exp(-t/0.05) + 1;
    i = env .* sin(2*pi*f*t - pi/2);
    i(i < 0) = 0.1*i(i < 0);
    fig = figure('Position',[100 100 800 400]);
    plot(t*1000, i, 'Color', palette('cat',1), 'LineWidth', 0.8); hold on;
    plot(t*1000, env, '--', 'Color', palette('cat',2), 'LineWidth', 1.2);
    xlabel('t (ms)'); ylabel('current (pu)'); title('Inrush current'); grid on;
end
