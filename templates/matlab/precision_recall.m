function fig = precision_recall()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    fig = figure; hold on;
    seps = [0.3 1.0 2.0];
    for i = 1:numel(seps)
        sep = seps(i);
        pos = randn(300, 1) + sep; neg = randn(700, 1);
        scores = [pos; neg]; y = [ones(300,1); zeros(700,1)];
        [~, idx] = sort(-scores); y = y(idx);
        tp = cumsum(y); fp = cumsum(1 - y);
        prec = tp ./ (tp + fp); rec = tp / sum(y);
        plot(rec, prec, 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('recall'); ylabel('precision'); title('Precision-Recall');
    legend(arrayfun(@(s)sprintf('sep=%.1f',s), seps, 'UniformOutput', false));
    grid on;
end
