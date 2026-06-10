function fig = multitaper_psd()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fs = 1000; N = 2048; t = (0:N-1)/fs;
    sig = sin(2*pi*50*t) + 0.5*sin(2*pi*120*t) + 0.3*randn(1,N);
    [tapers, ~] = dpss(N, 3, 5);
    psds = zeros(5, N/2+1);
    for k = 1:5
        S = abs(fft(sig(:) .* tapers(:, k))).^2;
        psds(k, :) = S(1:N/2+1);
    end
    psd = mean(psds, 1);
    psd_single = abs(fft(sig)).^2;
    f = (0:N/2) * fs/N;
    fig = figure;
    semilogy(f, psd_single(1:N/2+1), 'Color',[0.7 0.7 0.7], 'LineWidth', 0.8); hold on;
    semilogy(f, psd, 'Color', palette('cat',1), 'LineWidth', 1.5);
    xlim([0 200]); xlabel('frequency (Hz)'); ylabel('PSD');
    title('Multitaper PSD'); legend({'single taper','multitaper'}); grid on;
end
