function fig = weight_distribution()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    layers = {'conv1','conv2','fc1','fc2'};
    fig = figure('Position',[100 100 800 400]);
    for i = 1:4
        subplot(1, 4, i);
        init = 0.3*randn(2000, 1);
        trained = 0.05*(i-1) + (0.5-0.05*(i-1))*randn(2000, 1);
        histogram(init, 40, 'FaceColor',[0.8 0.8 0.8], 'EdgeColor','none', 'FaceAlpha', 0.6); hold on;
        histogram(trained, 40, 'FaceColor', palette('cat',i), 'EdgeColor','none', 'FaceAlpha', 0.6);
        title(layers{i}, 'FontSize', 10); legend({'init','trained'}, 'FontSize', 7); grid on;
    end
    sgtitle('Weight distribution');
end
