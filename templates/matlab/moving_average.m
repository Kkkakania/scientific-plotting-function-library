function fig = moving_average()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    t = 0:499; y = cumsum(randn(1, 500)) + 0.01*t;
    fig = figure('Position',[100 100 800 400]); hold on;
    plot(t, y, 'Color', [0.75 0.75 0.75], 'LineWidth', 0.8);
    for i = 1:3
        w = [5 20 60]; w = w(i);
        ma = filter(ones(1,w)/w, 1, y);
        plot(t, ma, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('t'); ylabel('value'); title('Moving averages');
    legend({'raw','MA(5)','MA(20)','MA(60)'}); grid on;
end
