function fig = nyquist_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat',1);
    K = 10; w = logspace(-2,2,5000); s = 1j*w;
    G = K ./ (s .* (s+1) .* (s+5));
    fig = figure('Position',[100 100 550 550]);
    plot(real(G), imag(G), 'Color', c, 'LineWidth', 1.5); hold on;
    plot(real(G), -imag(G), '--', 'Color', c, 'LineWidth', 1);
    plot(-1, 0, 'rx', 'MarkerSize', 12, 'LineWidth', 2);
    xline(0, 'Color', [0.6 0.6 0.6]); yline(0, 'Color', [0.6 0.6 0.6]);
    xlim([-3 1]); ylim([-2 2]); axis equal;
    xlabel('Re'); ylabel('Im'); title('Nyquist diagram');
    legend({'\omega>0','\omega<0','(-1,0)'}); grid on;
end
