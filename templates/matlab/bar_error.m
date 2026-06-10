function fig = bar_error()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    labels = {'A','B','C','D','E'};
    m = 30 + 50*rand(1,5); err = 3 + 7*rand(1,5);
    fig = figure;
    bar(m, 'FaceColor', palette('cat',1)); hold on;
    errorbar(1:5, m, err, 'k.', 'LineWidth', 1.2, 'CapSize', 8);
    set(gca,'XTickLabel',labels);
    ylabel('value'); title('Bar with error'); grid on;
end
