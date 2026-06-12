function fig = cusum_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    k = 0.5; h = 5.0; n = 60;
    x = randn(1, n);
    x(36:end) = x(36:end) + 1.0;               % injected small mean shift
    cp = zeros(1, n); cm = zeros(1, n);
    for i = 2:n
        cp(i) = max(0, cp(i-1) + x(i) - k);
        cm(i) = min(0, cm(i-1) + x(i) + k);
    end
    t = 0:n-1;
    c0 = palette('cat', 1); c1 = palette('cat', 2);
    c5 = palette('cat', 6); c7 = palette('cat', 8);
    fig = figure; hold on;
    h1 = plot(t, cp, '-o', 'Color', c0, 'MarkerSize', 3.5, 'MarkerFaceColor', c0);
    h2 = plot(t, cm, '-s', 'Color', c5, 'MarkerSize', 3.5, 'MarkerFaceColor', c5);
    h3 = yline(h, '--', 'Color', c7, 'LineWidth', 1);
    yline(-h, '--', 'Color', c7, 'LineWidth', 1);
    yline(0, '-', 'Color', [0.4 0.4 0.4], 'LineWidth', 0.8);
    up_out = cp > h; lo_out = cm < -h;
    hands = [h1 h2 h3];
    labs = {'C+ (upper)', 'C- (lower)', 'decision limit \pm h'};
    if any(up_out)
        h4 = plot(t(up_out), cp(up_out), 'o', 'Color', c1, ...
                  'MarkerFaceColor', c1, 'MarkerSize', 6);
        hands(end+1) = h4; labs{end+1} = 'signal';
    end
    if any(lo_out)
        plot(t(lo_out), cm(lo_out), 's', 'Color', c1, ...
             'MarkerFaceColor', c1, 'MarkerSize', 6);
    end
    xlabel('sample number'); ylabel('cumulative sum (standardized)');
    title('CUSUM control chart');
    legend(hands, labs, 'Location', 'northwest', 'FontSize', 7);
    grid on;
end
