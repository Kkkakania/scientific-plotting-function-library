function fig = dual_yaxis()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = 0:23;
    y1 = 20 + 8*sin((t-6)*pi/12); y2 = 60 - 20*sin((t-6)*pi/12);
    fig = figure;
    yyaxis left;  plot(t, y1, '-o', 'Color', palette('cat',1), ...
                        'MarkerFaceColor', palette('cat',1));
    ylabel('Y1'); set(gca,'YColor', palette('cat',1));
    yyaxis right; plot(t, y2, '-s', 'Color', palette('cat',2), ...
                        'MarkerFaceColor', palette('cat',2));
    ylabel('Y2'); set(gca,'YColor', palette('cat',2));
    xlabel('t'); title('Dual Y-axis'); grid on;
end
