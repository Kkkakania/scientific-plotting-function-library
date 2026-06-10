function fig = root_locus()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    poles = [0 -2 -5]; Ks = logspace(-1, 2.3, 80);
    locus = zeros(numel(Ks), 3);
    for i = 1:numel(Ks)
        coefs = real(poly(poles)); coefs(end) = coefs(end) + Ks(i);
        locus(i, :) = roots(coefs).';
    end
    fig = figure('Position',[100 100 600 500]); hold on;
    for j = 1:3
        scatter(real(locus(:, j)), imag(locus(:, j)), 12, Ks, 'filled');
    end
    plot(poles, zeros(size(poles)), 'rx', 'MarkerSize', 12, 'LineWidth', 2);
    colormap(palette('seq_blue'));
    xline(0,'Color',[0.6 0.6 0.6]); yline(0,'Color',[0.6 0.6 0.6]);
    xlabel('Re'); ylabel('Im'); title('Root locus'); grid on;
end
