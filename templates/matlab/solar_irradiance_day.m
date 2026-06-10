function fig = solar_irradiance_day()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    t = linspace(0, 24, 600);
    clear_sky = 950*exp(-0.5*((t - 12.5)/3.1).^2) .* (abs(t - 12.5) < 7.5);
    cloud_mod = 1 - 0.55*max(sin(t*2.1) + 0.4*sin(t*5.3 + 1), 0);
    cloudy = clear_sky .* min(max(cloud_mod + 0.05*randn(size(t)), 0.1), 1);
    rainy = 0.25*clear_sky .* min(max(1 + 0.15*randn(size(t)), 0.3), 1.4);
    curves = {clear_sky, cloudy, rainy}; labels = {'clear', 'cloudy', 'rainy'};
    fig = figure; hold on;
    for i = 1:3
        c = palette('cat', i);
        plot(t, curves{i}, 'Color', c, 'DisplayName', labels{i});
        fill([t fliplr(t)], [zeros(size(t)) fliplr(curves{i})], c, ...
             'FaceAlpha', 0.12, 'EdgeColor', 'none', 'HandleVisibility', 'off');
    end
    xlabel('hour of day'); ylabel('irradiance (W/m^2)');
    title('Daily solar irradiance profiles'); xlim([4 21]); legend; grid on;
end
