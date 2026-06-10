function fig = confusion_per_class()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(9);
    n = 8;
    classes = arrayfun(@(i)sprintf('cls %d',i), 1:n, 'UniformOutput', false);
    precision = 0.6 + 0.35*rand(1, n);
    recall = 0.6 + 0.35*rand(1, n);
    f1 = 2*precision.*recall ./ (precision + recall);
    fig = figure;
    bar([precision; recall; f1]', 'grouped');
    colormap([palette('cat',1); palette('cat',2); palette('cat',3)]);
    set(gca,'XTickLabel',classes);
    ylim([0 1]); ylabel('score'); title('Per-class metrics');
    legend({'precision','recall','F1'}); grid on;
end
