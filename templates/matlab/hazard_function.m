function fig = hazard_function()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    lam = 2.0;
    shapes = [0.5 1.0 1.5 2.5];
    labels = {'k = 0.5, decreasing (early failures)', ...
              'k = 1, constant (random)', ...
              'k = 1.5, increasing', ...
              'k = 2.5, strongly increasing (wear-out)'};
    t = linspace(0.02, 6, 400);
    fig = figure; hold on;
    for i = 1:numel(shapes)
        k = shapes(i);
        h = (k/lam) * (t/lam).^(k - 1);       % Weibull hazard rate
        plot(t, h, 'Color', palette('cat', i), 'LineWidth', 1.5);
    end
    ylim([0 2.0]);
    xlabel('time'); ylabel('hazard rate h(t)'); title('Weibull hazard functions');
    legend(labels, 'Location', 'north');
    grid on;
end
