function fig = envelope_detect()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 5000; t = 0:1/fs:0.5;
    env = 1 + 0.5*cos(2*pi*5*t);
    sig = env .* sin(2*pi*80*t);
    analytic = hilbert(sig);
    fig = figure('Position',[100 100 800 400]);
    plot(t*1000, sig, 'Color', [0.7 0.7 0.7], 'LineWidth', 0.7); hold on;
    plot(t*1000, abs(analytic), 'Color', palette('cat',1), 'LineWidth', 1.5);
    xlabel('t (ms)'); ylabel('amplitude'); title('Hilbert envelope');
    legend({'signal','|envelope|'}); grid on;
end
