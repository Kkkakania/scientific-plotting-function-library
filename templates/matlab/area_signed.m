function fig = area_signed()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 4*pi, 300); y = sin(x) .* exp(-x/8);
    fig = figure('Position',[100 100 800 350]); hold on;
    pos = y; pos(pos < 0) = 0; neg = y; neg(neg > 0) = 0;
    fill([x, fliplr(x)], [pos, zeros(size(pos))], palette('cat',1), 'FaceAlpha', 0.6, 'EdgeColor','none');
    fill([x, fliplr(x)], [neg, zeros(size(neg))], palette('cat',2), 'FaceAlpha', 0.6, 'EdgeColor','none');
    plot(x, y, 'k', 'LineWidth', 0.8); yline(0, 'k');
    xlabel('t'); ylabel('value'); title('Signed area');
    legend({'positive','negative'}); grid on;
end
