function fig = bar_grouped()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    labels = {'A','B','C','D','E'}; V = 10 + 70*rand(3, 5);
    fig = figure; b = bar(V', 'grouped');
    for k = 1:numel(b), b(k).FaceColor = palette('cat', k); end
    set(gca,'XTickLabel',labels);
    ylabel('value'); title('Grouped bar');
    legend({'2023','2024','2025'}); grid on;
end
