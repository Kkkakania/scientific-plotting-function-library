function fig = spectral_estimation_compare()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fs = 1000; N = fs; t = (0:N-1)/fs;
    sig = sin(2*pi*50*t) + 0.7*sin(2*pi*130*t) + 0.4*randn(1,N);
    [Pp, fp] = periodogram(sig, [], [], fs);         % 非参数法
    [Pb, fb] = pburg(sig, 24, [], fs);               % 参数法 Burg AR(24)
    fig = figure;
    semilogy(fp, Pp + 1e-12, 'Color', palette('cat',8), 'LineWidth', 1); hold on;
    semilogy(fb, Pb + 1e-12, 'Color', palette('cat',2), 'LineWidth', 2);
    xlabel('frequency (Hz)'); ylabel('PSD (V^2/Hz)');
    xlim([0 fs/2]); title('Spectral estimation: periodogram vs Burg AR');
    legend({'periodogram','Burg AR(24)'}, 'Box', 'off'); grid on;
end
