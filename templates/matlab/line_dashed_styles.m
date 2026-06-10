function fig = line_dashed_styles()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 10, 100);
    styles = {'-','--','-.',':'}; names = {'solid','dashed','dashdot','dotted'};
    fig = figure; hold on;
    for i = 1:4
        plot(x, sin(x) + (i-1)*0.6, styles{i}, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('y'); title('Line styles');
    legend(names); grid on;
end
