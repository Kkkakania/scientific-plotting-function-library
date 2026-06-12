function fig = interharmonic_spectrum()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    f1 = 50.0;
    % integer harmonics: typical 6-pulse drive pattern (5,7,11,13...) + noise floor
    h_orders = 2:19;
    h_amp = 0.15*ones(1, numel(h_orders));
    ks = [5 7 11 13 17]; av = [4.5 3.2 1.8 1.4 0.8];
    for j = 1:numel(ks)
        h_amp(h_orders == ks(j)) = av(j);
    end
    h_amp = h_amp + 0.1*rand(1, numel(h_orders));
    % interharmonics from a cycloconverter / doubly-fed drive: sidebands
    % at fi = |f_drive*k +/- f1*m| -- not integer multiples of 50 Hz
    ih_freq = [128 172 282 328 432 628];
    ih_amp = [0.9 0.7 0.55 0.4 0.3 0.2] + 0.05*rand(1, 6);
    w = 9;                                    % absolute bar width in Hz
    fig = figure('Position', [100 100 700 400]); hold on;
    hh = draw_bars(h_orders*f1, h_amp, w, palette('cat',1));
    hi = draw_bars(ih_freq, ih_amp, w, palette('cat',2));
    xlim([50 1000]);
    xlabel('frequency (Hz)'); ylabel('amplitude (% of fundamental)');
    title('Harmonic and interharmonic spectrum');
    legend([hh hi], {'integer harmonics', 'interharmonics'});
    grid on; set(gca, 'XGrid', 'off');
end

function h = draw_bars(xc, amp, w, c)
    m = numel(xc);
    X = [xc - w/2; xc + w/2; xc + w/2; xc - w/2];
    Y = [zeros(1, m); zeros(1, m); amp; amp];
    h = patch(X, Y, c, 'EdgeColor', 'none');
end
