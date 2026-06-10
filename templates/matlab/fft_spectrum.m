function fig = fft_spectrum()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fs = 1000; N = fs; t = (0:N-1)/fs;
    sig = sin(2*pi*50*t) + 0.6*sin(2*pi*120*t) + 0.3*randn(1,N);
    Y = fft(sig); amp = abs(Y(1:N/2+1))/N; amp(2:end-1) = 2*amp(2:end-1);
    f = (0:N/2) * fs/N;
    fig = figure('Position',[100 100 800 450]);
    subplot(2,1,1); plot(t(1:300), sig(1:300), 'Color', palette('cat',1));
    xlabel('t (s)'); ylabel('amp'); title('Time'); grid on;
    subplot(2,1,2); plot(f, amp, 'Color', palette('cat',2));
    xlim([0 250]); xlabel('frequency (Hz)'); ylabel('|Y|'); title('Spectrum'); grid on;
    sgtitle('FFT spectrum');
end
