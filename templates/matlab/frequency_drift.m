function fig = frequency_drift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    t = linspace(0, 60, 600);
    f = 50 + 0.03*sin(t/5) + 0.01*randn(size(t));
    f(300:340) = f(300:340) + 0.18;
    fig = figure('Position',[100 100 800 400]);
    fill([0 60 60 0], [49.95 49.95 50.05 50.05], [0 0.7 0], 'FaceAlpha', 0.15, 'EdgeColor','none'); hold on;
    plot(t, f, 'Color', palette('cat',1), 'LineWidth', 0.8);
    yline(50, 'Color', [0.5 0.5 0.5]);
    xlabel('t (s)'); ylabel('frequency (Hz)'); title('Grid frequency drift'); grid on;
end
