function fig = fir_design()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 1000; fc = 100; N = 51;
    b = fir1(N-1, fc/(fs/2), hamming(N));
    [h, w] = freqz(b, 1, 1024, fs);
    fig = figure('Position',[100 100 800 500]);
    subplot(2,1,1);
    stem(0:N-1, b, 'Color', palette('cat',1), 'MarkerFaceColor', palette('cat',1));
    xlabel('tap'); ylabel('coefficient'); title('FIR Impulse response'); grid on;
    subplot(2,1,2);
    plot(w, 20*log10(abs(h) + 1e-12), 'Color', palette('cat',1), 'LineWidth', 1.5);
    xline(fc, '--r', sprintf('fc=%d',fc));
    xlabel('frequency (Hz)'); ylabel('mag (dB)'); title('Frequency response'); grid on;
end
