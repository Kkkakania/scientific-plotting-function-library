function fig = iir_design()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 1000; fc = 100; order = 6;
    [b1, a1] = butter(order, fc/(fs/2));
    [b2, a2] = cheby1(order, 1, fc/(fs/2));
    [b3, a3] = cheby2(order, 40, fc/(fs/2));
    [b4, a4] = ellip(order, 1, 40, fc/(fs/2));
    fig = figure; hold on;
    nf = 1024;
    [h, w] = freqz(b1, a1, nf, fs); plot(w, 20*log10(abs(h)+1e-12), 'Color', palette('cat',1));
    [h, w] = freqz(b2, a2, nf, fs); plot(w, 20*log10(abs(h)+1e-12), 'Color', palette('cat',2));
    [h, w] = freqz(b3, a3, nf, fs); plot(w, 20*log10(abs(h)+1e-12), 'Color', palette('cat',3));
    [h, w] = freqz(b4, a4, nf, fs); plot(w, 20*log10(abs(h)+1e-12), 'Color', palette('cat',4));
    xline(fc, '--', 'Color', [0.5 0.5 0.5]);
    ylim([-80 5]); xlabel('frequency (Hz)'); ylabel('mag (dB)');
    title('IIR filter comparison');
    legend({'Butterworth','Cheby I','Cheby II','Elliptic'}); grid on;
end
