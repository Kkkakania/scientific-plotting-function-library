function fig = histogram_overlay()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fig = figure; hold on;
    for i = 1:3
        histogram(randn(500,1) + (i-2), 30, 'FaceColor', palette('cat',i), ...
                  'EdgeColor','w', 'FaceAlpha', 0.5);
    end
    xlabel('value'); ylabel('count'); title('Overlayed histograms');
    legend({'A','B','C'}); grid on;
end
