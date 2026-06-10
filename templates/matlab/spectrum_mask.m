function fig = spectrum_mask()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    f = linspace(-30, 30, 600);
    measured = -30 + 25*exp(-(f/5).^2) - 0.15*abs(f) + 1.5*randn(size(f));
    mask = zeros(size(f));
    mask(abs(f) < 9.5) = 0;
    mask(abs(f) >= 9.5 & abs(f) < 12) = -25;
    mask(abs(f) >= 12) = -45;
    fig = figure('Position',[100 100 800 400]);
    fill([f fliplr(f)], [mask 10*ones(size(mask))], 'r', 'FaceAlpha', 0.08, 'EdgeColor','none'); hold on;
    plot(f, measured, 'Color', palette('cat',1), 'LineWidth', 0.8);
    plot(f, mask, 'r', 'LineWidth', 1.5);
    xlabel('offset (MHz)'); ylabel('PSD (dBm/Hz)'); title('Spectrum mask');
    legend({'forbidden','measured','mask'}); grid on;
end
