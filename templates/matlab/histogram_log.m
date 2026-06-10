function fig = histogram_log()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(9);
    data = gprnd(0.5, 1, 1, 5000, 1) + 1;
    bins = logspace(0, log10(max(data)), 40);
    fig = figure;
    histogram(data, bins, 'FaceColor', palette('cat',1), 'EdgeColor','w');
    set(gca,'XScale','log','YScale','log');
    xlabel('value (log)'); ylabel('count (log)'); title('Log-bin histogram');
    grid on;
end
