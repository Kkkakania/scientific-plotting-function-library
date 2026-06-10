function fig = correlation_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    X = randn(200, 6);
    X(:,2) = 0.7*X(:,1) + 0.3*X(:,2);
    X(:,4) = -0.5*X(:,3) + 0.5*X(:,4);
    M = corrcoef(X);
    fig = figure; imagesc(M, [-1 1]);
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'r';
    n = size(M,1);
    for i = 1:n
        for j = 1:n
            if abs(M(i,j)) > 0.6, col = 'w'; else, col = 'k'; end
            text(j, i, sprintf('%.2f', M(i,j)), 'Color', col, ...
                 'HorizontalAlignment','center', 'FontSize', 7);
        end
    end
    names = arrayfun(@(i)sprintf('v%d',i),1:n,'UniformOutput',false);
    set(gca,'XTick',1:n,'XTickLabel',names,'YTick',1:n,'YTickLabel',names);
    title('Correlation matrix'); axis tight;
end
