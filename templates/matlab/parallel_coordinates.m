function fig = parallel_coordinates()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    data = rand(60, 6);
    cls = double(data(:,1) > 0.5);
    fig = figure('Position',[100 100 800 450]); hold on;
    x = 1:6;
    for i = 1:size(data,1)
        plot(x, data(i,:), 'Color', palette('cat', cls(i)+1), 'LineWidth', 1);
    end
    set(gca,'XTick',1:6,'XTickLabel',arrayfun(@(i)sprintf('d%d',i),1:6,'UniformOutput',false));
    ylabel('value'); title('Parallel coordinates'); grid on;
end
