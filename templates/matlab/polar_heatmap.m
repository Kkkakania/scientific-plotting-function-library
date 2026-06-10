function fig = polar_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    theta = linspace(0, 2*pi, 200);
    r = linspace(0, 1, 80);
    [T, R] = meshgrid(theta, r);
    Z = (1 + cos(4*T)) .* (1 - R.^2);
    [Xc, Yc] = pol2cart(T, R);
    fig = figure('Position',[100 100 600 600]);
    pcolor(Xc, Yc, Z); shading interp;
    colormap(hot); cb = colorbar; cb.Label.String = 'value';
    axis equal off; title('Polar density');
end
