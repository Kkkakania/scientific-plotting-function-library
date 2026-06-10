function fig = wavelet_scalogram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 500; t = 0:1/fs:1-1/fs;
    sig = sin(2*pi*20*t).*(t < 0.4) + sin(2*pi*80*t).*(t >= 0.4);
    freqs = logspace(log10(5), log10(120), 40);
    W = zeros(numel(freqs), numel(t));
    for i = 1:numel(freqs)
        f = freqs(i);
        N = floor(min(6*fs/f, numel(t)));
        n = -floor(N/2):ceil(N/2)-1;
        wlt = exp(2j*pi*f*n/fs) .* exp(-(n/fs).^2 .* (f^2) * 2);
        W(i, :) = abs(conv(sig, wlt, 'same'));
    end
    fig = figure('Position',[100 100 800 400]);
    pcolor(t, freqs, W); shading interp; set(gca,'YScale','log');
    colormap(hot); cb = colorbar; cb.Label.String = '|W|';
    xlabel('t (s)'); ylabel('frequency (Hz)'); title('Wavelet scalogram');
end
