function fig = voltage_sag()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = 50; fs = 5000; t = 0:1/fs:0.5;
    env = ones(size(t)); env(t >= 0.18 & t < 0.35) = 0.5;
    sig = env .* sin(2*pi*f*t);
    fig = figure('Position',[100 100 800 400]);
    plot(t*1000, sig, 'Color', palette('cat',1), 'LineWidth', 0.8); hold on;
    plot(t*1000, env, 'Color', palette('cat',2), 'LineWidth', 1.5);
    plot(t*1000, -env, 'Color', palette('cat',2), 'LineWidth', 1.5);
    xlabel('t (ms)'); ylabel('voltage (pu)'); title('Voltage sag event'); grid on;
end
