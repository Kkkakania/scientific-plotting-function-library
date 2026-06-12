function fig = spiral_timeseries()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(23);
    n_years = 3; n_w = 52;
    w = 0:(n_years * n_w - 1);
    val = 12 + 8 * sin((mod(w, n_w) - 6) * 2*pi / n_w) ...
        + 0.06 * w + 1.2 * randn(1, numel(w));
    theta = 2*pi * mod(w, n_w) / n_w;
    r = 1.0 + w / n_w;                               % one turn per year
    months = {'Jan','Feb','Mar','Apr','May','Jun', ...
              'Jul','Aug','Sep','Oct','Nov','Dec'};
    fig = figure('Position',[100 100 550 550]);
    pax = polaraxes; hold(pax, 'on');
    polarscatter(pax, theta, r, 22, val, 'filled');
    pax.ThetaZeroLocation = 'top';
    pax.ThetaDirection = 'clockwise';
    pax.ThetaTick = 0:30:330;
    pax.ThetaTickLabel = months;
    pax.RTick = [1.5 2.5 3.5];
    pax.RTickLabel = {'yr 1', 'yr 2', 'yr 3'};
    pax.RLim = [0 n_years + 1.3];
    pax.FontSize = 8;
    colormap(palette('seq_blue'));
    cb = colorbar; ylabel(cb, 'value');
    title('Time spiral (3 years, weekly)');
end
