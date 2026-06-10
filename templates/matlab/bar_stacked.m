function fig = bar_stacked()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    labels = {'A','B','C','D','E'}; V = 10 + 70*rand(5, 4);
    fig = figure; b = bar(V, 'stacked');
    for k = 1:numel(b), b(k).FaceColor = palette('cat', k); end
    set(gca,'XTickLabel',labels);
    ylabel('value'); title('Stacked bar');
    legend(arrayfun(@(i)sprintf('comp %d',i),1:4,'UniformOutput',false)); grid on;
end
