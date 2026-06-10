function fig = pwm_modulation()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 0.02, 5000);
    mod_w = 0.8 * sin(2*pi*50*t);
    carrier = (2/pi) * asin(sin(2*pi*1000*t));
    out = sign(mod_w - carrier);
    fig = figure('Position',[100 100 900 400]);
    plot(t*1000, carrier, 'Color',[0.7 0.7 0.7], 'LineWidth', 0.7); hold on;
    plot(t*1000, mod_w, 'Color', palette('cat',1), 'LineWidth', 1.5);
    plot(t*1000, out*0.6, 'Color', palette('cat',2), 'LineWidth', 0.8);
    xlabel('t (ms)'); ylabel('value'); title('Sinusoidal PWM');
    legend({'carrier','modulation','output'}); grid on;
end
