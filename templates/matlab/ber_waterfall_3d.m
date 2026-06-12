function fig = ber_waterfall_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    ebn0_db = linspace(0, 24, 49);
    ks = [2 4 6 8];
    names = {'QPSK', '16-QAM', '64-QAM', '256-QAM'};
    gam = 10.^(ebn0_db/10);
    Z = zeros(numel(ks), numel(ebn0_db));
    for i = 1:numel(ks)
        k = ks(i); M = 2^k;
        arg = sqrt(3*k*gam/(M-1));
        pb = 4/k*(1 - 1/sqrt(M))*0.5.*erfc(arg/sqrt(2));
        Z(i, :) = log10(min(max(pb, 1e-8), 0.5));
    end
    [X, Y] = meshgrid(ebn0_db, ks);
    fig = figure('Position', [100 100 680 520]);
    surf(X, Y, Z, 'EdgeColor', 'none', 'FaceAlpha', 0.75);
    colormap(parula); hold on;
    hh = gobjects(1, numel(ks));
    for i = 1:numel(ks)
        hh(i) = plot3(ebn0_db, ks(i)*ones(size(ebn0_db)), Z(i, :), ...
                      'Color', palette('cat', i), 'LineWidth', 1.8);
    end
    xlabel('E_b/N_0 (dB)'); ylabel('bits per symbol'); zlabel('log_{10}(BER)');
    yticks(ks);
    title('M-QAM BER surface');
    legend(hh, names, 'Location', 'northeast', 'FontSize', 7);
    view(-130, 25);
end
