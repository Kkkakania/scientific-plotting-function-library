function fig = welch_psd()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fs = 1000; N = fs; t = (0:N-1)/fs;
    sig = sin(2*pi*50*t) + 0.6*sin(2*pi*120*t) + 0.3*randn(1,N);
    [Pxx, f] = pwelch(sig, 256, [], [], fs);
    fig = figure;
    semilogy(f, Pxx, 'Color', palette('cat',1), 'LineWidth', 1.5);
    xlabel('frequency (Hz)'); ylabel('PSD'); title('Welch PSD'); grid on;
end
