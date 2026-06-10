function fig = impedance_locus(R, L, C)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    if nargin < 1, R = 10; end
    if nargin < 2, L = 0.1; end
    if nargin < 3, C = 1e-4; end
    w = logspace(0, 5, 400);
    Z = R + 1j*w*L + 1./(1j*w*C);
    f0 = 1/(2*pi*sqrt(L*C));
    fig = figure('Position',[100 100 600 500]);
    plot(real(Z), imag(Z), 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot(R, 0, 'rx', 'MarkerSize', 12, 'LineWidth', 2);
    yline(0, 'Color', [0.5 0.5 0.5]);
    xlabel('Re\{Z\}'); ylabel('Im\{Z\}');
    title('Impedance locus (series RLC)');
    legend({'Z(\omega)', sprintf('resonance (f=%.1f Hz)', f0)}); grid on;
end
