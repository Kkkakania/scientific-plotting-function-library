function fig = box_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    data = randn(100, 5) + [0 1 2 1.5 0.5];
    fig = figure; boxplot(data, 'Labels', {'A','B','C','D','E'});
    ylabel('value'); title('Box plot'); grid on;
end
