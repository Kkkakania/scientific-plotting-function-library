function fig = constellation(snr_db)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    if nargin<1, snr_db = 20; end
    apply_theme(); rng(0);
    [I, Q] = meshgrid([-3 -1 1 3]);
    pts = [I(:) Q(:)];
    n = 800; idx = randi(16, n, 1); tx = pts(idx, :);
    snr = 10^(snr_db/10);
    es = mean(sum(pts.^2, 2)); n0 = es / snr;
    noise = sqrt(n0/2) * randn(n, 2);
    rx = tx + noise;
    fig = figure('Position',[100 100 550 550]);
    scatter(rx(:, 1), rx(:, 2), 8, palette('cat',1), 'filled', 'MarkerFaceAlpha', 0.4); hold on;
    scatter(pts(:, 1), pts(:, 2), 80, 'r', '+', 'LineWidth', 2);
    xlabel('I'); ylabel('Q'); axis equal;
    title(sprintf('16-QAM constellation (SNR=%d dB)', snr_db));
    grid on;
end
