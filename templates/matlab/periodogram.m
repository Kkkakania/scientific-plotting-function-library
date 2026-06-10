function fig = periodogram_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    fs = 1000; N = 4096;
    sig = sin(2*pi*60*(0:N-1)/fs) + 0.6*randn(1,N);
    [p1, f1] = periodogram(sig, [], [], fs);
    [p2, f2] = pwelch(sig, 512, [], [], fs);
    fig = figure;
    semilogy(f1, p1, 'Color',[0.7 0.7 0.7], 'LineWidth', 0.7); hold on;
    semilogy(f2, p2, 'Color', palette('cat',1), 'LineWidth', 1.5);
    xlabel('frequency (Hz)'); ylabel('PSD');
    title('Periodogram vs Welch'); legend({'periodogram','Welch'}); grid on;
end
