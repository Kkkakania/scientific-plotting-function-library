function fig = qam_constellation_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    snr_db = 24; n_sym = 1500;
    Ms = [4 16 64 256];
    fig = figure('Position',[100 100 680 660]);
    for k = 1:4
        M = Ms(k); m = sqrt(M);
        lv = 2*(0:m-1) - (m - 1);
        [Ig, Qg] = meshgrid(lv, lv);
        pts = Ig(:) + 1i*Qg(:);
        pts = pts / sqrt(mean(abs(pts).^2));         % unit average power
        tx = pts(randi(M, n_sym, 1));
        sigma = sqrt(10^(-snr_db/10) / 2);
        rx = tx + sigma * (randn(n_sym,1) + 1i*randn(n_sym,1));
        evm = 100 * sqrt(mean(abs(rx - tx).^2) / mean(abs(pts).^2));
        subplot(2, 2, k); hold on;
        scatter(real(rx), imag(rx), 3, palette('cat',1), 'filled', ...
                'MarkerFaceAlpha', 0.35);
        scatter(real(pts), imag(pts), 14, palette('cat',2), '+', 'LineWidth', 0.9);
        text(-1.6, 1.55, sprintf('EVM = %.1f%%', evm), 'FontSize', 8);
        title(sprintf('%d-QAM', M), 'FontSize', 9);
        xlabel('I'); ylabel('Q');
        axis equal; xlim([-1.7 1.7]); ylim([-1.7 1.7]);
        grid on;
    end
    sgtitle(sprintf('QAM constellations (SNR = %d dB)', snr_db));
end
