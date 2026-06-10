function fig = confidence_band()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 10, 100);
    means = {sin(x), cos(x), 0.5*sin(2*x)};
    stds  = {0.15+0*x, 0.2+0*x, 0.1+0*x};
    fig = figure; hold on;
    for i = 1:3
        c = palette('cat', i);
        fill([x, fliplr(x)], [means{i}+stds{i}, fliplr(means{i}-stds{i})], c, ...
             'FaceAlpha', 0.2, 'EdgeColor','none');
        plot(x, means{i}, 'Color', c, 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('y'); title('Group means \pm std');
    legend({'','A','','B','','C'}); grid on;
end
