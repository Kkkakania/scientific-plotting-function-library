function fig = partial_dependence()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    x = linspace(0, 1, 100);
    pdps = {log(x + 0.1) + 1.5 + 0.05*randn(1, 100), ...
            2*x - x.^2 + 0.05*randn(1, 100), ...
            sin(3*pi*x) + 0.05*randn(1, 100), ...
            double(x > 0.5) + 0.05*randn(1, 100)};
    fig = figure('Position',[100 100 800 400]);
    for i = 1:4
        subplot(1, 4, i);
        plot(x, pdps{i}, 'Color', palette('cat',i), 'LineWidth', 1.5);
        xlabel(sprintf('feat_%d', i));
        if i == 1, ylabel('partial dependence'); end
        grid on;
    end
    sgtitle('Partial dependence');
end
