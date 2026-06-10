function fig = bar_horizontal()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    labels = arrayfun(@(i)sprintf('option %d',i),1:8,'UniformOutput',false);
    v = sort(10 + 80*rand(1, 8));
    fig = figure; barh(v, 'FaceColor', palette('cat',2));
    set(gca,'YTickLabel',labels);
    xlabel('value'); title('Horizontal bar'); grid on;
end
