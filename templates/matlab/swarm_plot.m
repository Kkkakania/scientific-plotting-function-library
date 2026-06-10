function fig = swarm_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    groups = {randn(60,1), randn(60,1)+1.5, randn(60,1)+1, randn(60,1)+0.5};
    fig = figure; hold on;
    for i = 1:numel(groups)
        arr = sort(groups{i});
        x = ones(size(arr))*i; offset = 0;
        for j = 2:numel(arr)
            if arr(j) - arr(j-1) < 0.15
                offset = -offset + 0.06 * sign(-offset + eps);
                x(j) = i + offset;
            else
                offset = 0;
            end
        end
        scatter(x, arr, 22, palette('cat',i), 'filled', 'MarkerFaceAlpha', 0.8, 'MarkerEdgeColor','w');
    end
    set(gca,'XTick',1:4,'XTickLabel',{'A','B','C','D'});
    ylabel('value'); title('Swarm plot'); grid on;
end
