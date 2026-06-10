function fig = bar_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    labels = {'A','B','C','D','E','F'}; v = 10 + 70*rand(1,6);
    fig = figure; bar(v, 'FaceColor', palette('cat',1));
    set(gca,'XTickLabel',labels);
    ylabel('value'); title('Bar plot'); grid on;
end
