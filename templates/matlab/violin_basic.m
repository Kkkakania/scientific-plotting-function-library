function fig = violin_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    fig = figure; hold on;
    for i = 1:4
        arr = randn(300,1) + (i-1)*0.5;
        [f, xi] = ksdensity(arr);
        f = f / max(f) * 0.4;
        fill([i+f, i-fliplr(f)], [xi, fliplr(xi)], palette('cat',i), ...
             'FaceAlpha', 0.5, 'EdgeColor', palette('cat',i));
        plot([i i], [median(arr) median(arr)], 'k+', 'MarkerSize', 10);
    end
    set(gca,'XTick',1:4,'XTickLabel',{'A','B','C','D'});
    ylabel('value'); title('Violin plot'); grid on;
end
