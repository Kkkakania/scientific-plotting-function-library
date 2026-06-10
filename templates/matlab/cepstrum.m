function fig = cepstrum()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fs = 8000; t = 0:1/fs:0.1; f0 = 200;
    sig = zeros(size(t));
    for k = 0:7, sig = sig + 0.6^k * sin(2*pi*(k+1)*f0*t); end
    sig = sig + 0.05*randn(size(t));
    spec = fft(sig);
    log_mag = log(abs(spec) + 1e-12);
    cep = real(ifft(log_mag));
    quef = (0:numel(cep)-1) / fs * 1000;
    fig = figure('Position',[100 100 800 400]);
    plot(quef, cep, 'Color', palette('cat',1)); hold on;
    xline(1000/f0, '--r', sprintf('1/f_0 = %.1f ms', 1000/f0));
    xlim([0 20]); xlabel('quefrency (ms)'); ylabel('cepstrum');
    title('Cepstrum'); grid on;
end
