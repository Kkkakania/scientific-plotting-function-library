function fig = dq_transform()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = 50; t = linspace(0, 0.1, 1000); w = 2*pi*f;
    a = sin(w*t); b = sin(w*t - 2*pi/3); c = sin(w*t + 2*pi/3);
    theta = w*t;
    d = (2/3)*(a.*cos(theta) + b.*cos(theta - 2*pi/3) + c.*cos(theta + 2*pi/3));
    q = -(2/3)*(a.*sin(theta) + b.*sin(theta - 2*pi/3) + c.*sin(theta + 2*pi/3));
    fig = figure('Position',[100 100 800 500]);
    subplot(2,1,1); plot(t*1000, a, 'Color', palette('cat',1)); hold on;
    plot(t*1000, b, 'Color', palette('cat',2)); plot(t*1000, c, 'Color', palette('cat',3));
    ylabel('abc'); legend({'a','b','c'}); grid on; title('abc → dq0 transform');
    subplot(2,1,2); plot(t*1000, d, 'Color', palette('cat',4)); hold on;
    plot(t*1000, q, 'Color', palette('cat',5));
    xlabel('t (ms)'); ylabel('dq'); legend({'d','q'}); grid on;
end
