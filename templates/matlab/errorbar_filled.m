function fig = errorbar_filled()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1); c = palette('cat',1);
    x = linspace(0, 10, 100); trials = sin(x) + 0.15*randn(30, 100);
    m = mean(trials,1); s = std(trials,0,1);
    fig = figure;
    fill([x, fliplr(x)], [m+s, fliplr(m-s)], c, 'FaceAlpha', 0.25, 'EdgeColor','none'); hold on;
    plot(x, m, 'Color', c, 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Mean with band'); grid on;
end
