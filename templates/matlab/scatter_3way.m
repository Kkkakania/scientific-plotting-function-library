function fig = scatter_3way()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    n = 60; x = 10*rand(n,1); y = 10*rand(n,1);
    s = 40 + 360*rand(n,1); g = randi(3, n, 1);
    markers = {'o','s','^'};
    fig = figure; hold on;
    for k = 1:3
        m = g == k;
        scatter(x(m), y(m), s(m), palette('cat',k), 'filled', markers{k}, ...
                'MarkerFaceAlpha', 0.6, 'MarkerEdgeColor','k');
    end
    xlabel('x'); ylabel('y'); title('3-encoded scatter');
    legend({'class 1','class 2','class 3'}); grid on;
end
