function fig = timeseries_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    t = 0:364; y = 0.001*t + sin(2*pi*t/30) + 0.2*randn(1, 365);
    fig = figure('Position',[100 100 800 350]);
    plot(t, y, 'Color', palette('cat',1), 'LineWidth', 1);
    xlabel('day'); ylabel('value'); title('Time series'); grid on;
end
