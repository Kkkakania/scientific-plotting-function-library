function fig = returns_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(14);
    years = 2018:2025;
    months = {'Jan','Feb','Mar','Apr','May','Jun', ...
              'Jul','Aug','Sep','Oct','Nov','Dec'};
    ny = numel(years);
    R = 0.8 + 3.5 * randn(ny, 12);                     % monthly returns in percent
    vmax = max(abs(R(:)));
    fig = figure('Position',[100 100 700 400]);
    imagesc(R); hold on;
    colormap(palette('div'));
    caxis([-vmax vmax]);
    for i = 1:ny
        for j = 1:12
            v = R(i, j);
            if abs(v) > 0.6 * vmax, tc = [1 1 1]; else, tc = [0.2 0.2 0.2]; end
            text(j, i, sprintf('%.0f', v), 'HorizontalAlignment', 'center', ...
                 'VerticalAlignment', 'middle', 'FontSize', 6.5, 'Color', tc);
        end
    end
    set(gca, 'XTick', 1:12, 'XTickLabel', months, ...
             'YTick', 1:ny, 'YTickLabel', years, 'FontSize', 8);
    xlabel('month'); ylabel('year');
    title('Monthly returns heatmap');
    cb = colorbar; ylabel(cb, 'return (%)');
end
