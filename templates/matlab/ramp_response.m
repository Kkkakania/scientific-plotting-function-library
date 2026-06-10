function fig = ramp_response()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 8, 500); tau = 1;
    y1 = t - tau + tau*exp(-t/tau);
    z = 0.5; wn = 2; wd = wn*sqrt(1 - z^2);
    y2 = t - 2*z/wn + exp(-z*wn*t).*(2*z/wn*cos(wd*t) - (1-2*z^2)/wd*sin(wd*t));
    fig = figure;
    plot(t, t, '--', 'Color', [0.5 0.5 0.5]); hold on;
    plot(t, y1, 'Color', palette('cat',1), 'LineWidth', 1.5);
    plot(t, y2, 'Color', palette('cat',2), 'LineWidth', 1.5);
    xlabel('t'); ylabel('y(t)'); title('Ramp response');
    legend({'input','1st-order','2nd-order'}); grid on;
end
