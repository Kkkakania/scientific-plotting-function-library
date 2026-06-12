function fig = array_factor_polar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    elements = [4 8 16]; d = 0.5; floor_db = -40;
    theta = linspace(-pi, pi, 1441);
    fig = figure('Position', [100 100 600 600]);
    pax = polaraxes; hold(pax, 'on');
    for i = 1:numel(elements)
        n = elements(i);
        psi = 2*pi*d*sin(theta);
        den = n*sin(psi/2);
        af = abs(sin(n*psi/2) ./ den);
        af(abs(den) < 1e-9) = 1.0;
        db = min(max(20*log10(af + 1e-9), floor_db), 0);
        polarplot(pax, theta, db - floor_db, 'Color', palette('cat', i), ...
                  'LineWidth', 1.5, 'DisplayName', sprintf('N=%d', n));
    end
    pax.ThetaZeroLocation = 'top';
    pax.RLim = [0 -floor_db]; pax.RTick = [10 20 30 40];
    pax.RTickLabel = {'-30', '-20', '-10', '0 dB'};
    title('Uniform linear array factor (d=0.5\lambda)');
    legend('Location', 'southoutside', 'Orientation', 'horizontal');
end
