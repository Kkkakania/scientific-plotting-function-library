function fig = histogram_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    fig = figure; hold on;
    locs = [0 1.5 -1];
    for i = 1:3
        histogram(randn(1000,1) + locs(i), 40, 'DisplayStyle','stairs', ...
                  'EdgeColor', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('value'); ylabel('count'); title('Step histogram');
    legend({'A','B','C'}); grid on;
end
