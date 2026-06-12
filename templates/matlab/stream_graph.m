function fig = stream_graph()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    n = 200; n_series = 5;
    x = linspace(0, 24, n);
    Y = zeros(n_series, n);
    for i = 1:n_series
        for b = 1:4                  % each stream = sum of gaussian bumps
            c = 2 + 20*rand; wdt = 1.5 + 3.5*rand; a = 0.5 + 1.5*rand;
            Y(i, :) = Y(i, :) + a * exp(-0.5 * ((x - c) / wdt).^2);
        end
    end
    base = -sum(Y, 1) / 2;           % wiggle baseline, symmetric silhouette
    layers = [zeros(1, n); cumsum(Y, 1)] + base;
    fig = figure('Position',[100 100 800 400]); hold on;
    hs = gobjects(1, n_series); labels = cell(1, n_series);
    for i = 1:n_series
        hs(i) = fill([x fliplr(x)], [layers(i,:) fliplr(layers(i+1,:))], ...
                     palette('cat',i), 'FaceAlpha', 0.85, ...
                     'EdgeColor', [1 1 1], 'LineWidth', 0.5);
        labels{i} = sprintf('topic %d', i);
    end
    xlabel('time (month)'); ylabel('flow magnitude');
    title('Stream graph');
    legend(hs, labels, 'Location', 'southoutside', 'Orientation', ...
           'horizontal', 'Box', 'off');
    set(gca, 'XGrid', 'on', 'YGrid', 'off');
end
