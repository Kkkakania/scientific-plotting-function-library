function fig = lfm_chirp()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    B = 6e6; T = 8e-6; K = B/T; fs = 5*B;     % 带宽/脉宽/调频斜率/采样率
    t = -T/2:1/fs:T/2;
    st = exp(1j*pi*K*t.^2);                   % 复包络
    f_inst = K*t;                             % 瞬时频率
    fig = figure;
    subplot(2,2,1);
    plot(t*1e6, real(st), 'Color', palette('cat',1), 'LineWidth', 1);
    title('real part'); xlabel('t (us)'); ylabel('amplitude'); grid on;
    subplot(2,2,2);
    plot(t*1e6, imag(st), 'Color', palette('cat',2), 'LineWidth', 1);
    title('imag part'); xlabel('t (us)'); ylabel('amplitude'); grid on;
    subplot(2,2,3);
    plot(t*1e6, f_inst*1e-6, 'Color', palette('cat',3), 'LineWidth', 2);
    title('instantaneous freq'); xlabel('t (us)'); ylabel('f (MHz)'); grid on;
    subplot(2,2,4);
    [S,f,tt] = spectrogram(real(st), 64, 56, 64, fs);
    pcolor(tt*1e6, f*1e-6, 10*log10(abs(S)+1e-12)); shading interp;
    colormap(palette('seq_blue', 256)); colorbar;
    title('STFT (dB)'); xlabel('t (us)'); ylabel('f (MHz)');
end
