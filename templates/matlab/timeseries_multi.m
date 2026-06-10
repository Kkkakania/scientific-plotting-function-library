function fig = timeseries_multi()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    t = 0:364;
    fig = figure('Position',[100 100 800 400]); hold on;
    for i = 1:4
        y = 0.001*t + sin(2*pi*t/30 + i) + 0.2*randn(1,365) + (i-1)*0.5;
        plot(t, y, 'Color', palette('cat',i), 'LineWidth', 1);
    end
    xlabel('day'); ylabel('value'); title('Multi-series time');
    legend(arrayfun(@(i)sprintf('series %d',i),1:4,'UniformOutput',false));
    grid on;
end
