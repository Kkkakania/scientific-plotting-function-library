function fig = ridgeline()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(8);
    fig = figure('Position',[100 100 700 500]); hold on;
    locs = linspace(0, 4, 6);
    for i = 1:6
        arr = randn(400,1) + locs(i);
        [f, xi] = ksdensity(arr, linspace(-4,8,200));
        f = f / max(f) * 0.8;
        fill([xi, fliplr(xi)], [i + f, i*ones(size(xi))], palette('cat',i), ...
             'FaceAlpha', 0.7, 'EdgeColor','w');
    end
    set(gca,'YTick',1:6,'YTickLabel',arrayfun(@(i)sprintf('group %d',i),1:6,'UniformOutput',false));
    xlabel('value'); title('Ridgeline'); grid on;
end
