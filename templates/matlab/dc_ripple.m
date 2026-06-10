function fig = dc_ripple()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 5000; t = 0:1/fs:0.04;
    ac = abs(sin(2*pi*50*t)) * 311;
    [b, a] = butter(4, 30/(fs/2), 'low');
    dc = filtfilt(b, a, ac);
    fig = figure('Position',[100 100 800 400]);
    plot(t*1000, ac, 'Color',[0.7 0.7 0.7], 'LineWidth', 1); hold on;
    plot(t*1000, dc, 'Color', palette('cat',1), 'LineWidth', 1.5);
    xlabel('t (ms)'); ylabel('voltage (V)'); title('DC ripple before/after filter');
    legend({'rectified','after filter'}); grid on;
end
