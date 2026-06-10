function fig = coherence_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    fs = 1000; n = 4096; common = sin(2*pi*70*(0:n-1)/fs);
    x = common + 0.7*randn(1,n); y = 0.8*common + 0.7*randn(1,n);
    [Cxy, f] = mscohere(x, y, [], [], 512, fs);
    fig = figure;
    plot(f, Cxy, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    xline(70, '--r', 'common 70 Hz');
    xlim([0 250]); xlabel('frequency (Hz)'); ylabel('coherence');
    title('Magnitude-squared coherence'); grid on;
end
