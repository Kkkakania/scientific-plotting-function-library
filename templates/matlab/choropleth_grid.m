function fig = choropleth_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    grid = rand(8, 12);
    fig = figure('Position',[100 100 700 500]);
    imagesc(grid); colormap(palette('seq_blue'));
    cb = colorbar; cb.Label.String = 'rate';
    set(gca,'XTick',1:12,'XTickLabel',arrayfun(@(j)sprintf('C%d',j),1:12,'UniformOutput',false), ...
            'YTick',1:8, 'YTickLabel',arrayfun(@(i)sprintf('R%d',i),1:8,'UniformOutput',false));
    title('Choropleth grid');
end
