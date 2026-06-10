function fig = antenna_pattern_polar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    theta = linspace(0, 2*pi, 720);
    fig = figure('Position',[100 100 600 600]);
    pax = polaraxes; hold(pax, 'on');
    for i = 1:3
        N = 2^i;
        psi = pi * cos(theta);
        gain = abs(sin(N*psi/2) ./ (N*sin(psi/2) + 1e-12));
        dB = 20*log10(gain + 1e-6); dB = max(dB, -40);
        polarplot(pax, theta, dB + 40, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    pax.RLim = [0 40]; pax.RTick = [10 20 30 40];
    pax.RTickLabel = {'-30','-20','-10','0 dB'};
    title('Antenna pattern');
    legend({'N=2','N=4','N=8'}, 'Location','southoutside');
end
