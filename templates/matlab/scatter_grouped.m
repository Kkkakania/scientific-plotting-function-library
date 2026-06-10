function fig = scatter_grouped()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fig = figure; hold on;
    for k = 1:3
        x = randn(80,1) + (k-1)*2.5; y = randn(80,1) + (k-1)*2.5;
        scatter(x, y, 30, palette('cat',k), 'filled', 'MarkerFaceAlpha', 0.7, ...
                'MarkerEdgeColor','w');
    end
    xlabel('feature 1'); ylabel('feature 2'); title('Grouped scatter');
    legend({'class 0','class 1','class 2'}); grid on;
end
