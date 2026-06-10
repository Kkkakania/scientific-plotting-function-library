function fig = load_curve_daily()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat',1);
    h = 0:23;
    load_v = 50 + 20*sin((h-6)*pi/12) + 15*exp(-((h-19).^2)/8);
    fig = figure('Position',[100 100 800 400]);
    plot(h, load_v, '-o', 'Color', c, 'MarkerFaceColor', c); hold on;
    fill([h fliplr(h)], [load_v zeros(size(load_v))], c, 'FaceAlpha', 0.2, 'EdgeColor','none');
    [pk, ipk] = max(load_v); [tr, itr] = min(load_v);
    scatter(h(ipk), pk, 80, 'r', 'filled'); scatter(h(itr), tr, 80, 'g', 'filled');
    xlabel('hour'); ylabel('load (MW)'); title('Daily load profile');
    xticks(0:3:24); grid on;
end
