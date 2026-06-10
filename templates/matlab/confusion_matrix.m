function fig = confusion_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    M = [42 3 1 0; 4 38 2 1; 1 5 36 2; 0 2 3 40];
    Mn = M ./ sum(M, 2);
    fig = figure; imagesc(Mn, [0 1]);
    colormap(palette('seq_blue')); cb = colorbar; cb.Label.String = 'proportion';
    for i = 1:4
        for j = 1:4
            if Mn(i,j) > 0.5, col = 'w'; else, col = 'k'; end
            text(j, i, sprintf('%d', M(i,j)), 'Color', col, ...
                 'HorizontalAlignment','center');
        end
    end
    set(gca,'XTick',1:4,'XTickLabel',{'A','B','C','D'}, ...
            'YTick',1:4,'YTickLabel',{'A','B','C','D'});
    xlabel('predicted'); ylabel('true'); title('Confusion matrix'); axis tight;
end
