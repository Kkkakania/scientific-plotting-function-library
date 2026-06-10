function fig = matrix_correlogram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(15);
    X = randn(200, 7);
    X(:,2) = 0.7*X(:,1) + 0.3*X(:,2);
    X(:,4) = -0.5*X(:,3) + 0.5*X(:,4);
    M = corrcoef(X); n = size(M,1);
    [Y, Xi] = ndgrid(1:n, 1:n);
    fig = figure('Position',[100 100 600 600]);
    scatter(Xi(:), Y(:), 700*abs(M(:)), M(:), 'filled', ...
            'MarkerEdgeColor','w', 'LineWidth', 0.5);
    colormap(palette('div')); caxis([-1 1]);
    cb = colorbar; cb.Label.String = 'r';
    names = arrayfun(@(i)sprintf('v%d',i),1:n,'UniformOutput',false);
    set(gca,'XTick',1:n,'XTickLabel',names,'YTick',1:n,'YTickLabel',names, ...
            'YDir','reverse');
    title('Correlogram');
end
