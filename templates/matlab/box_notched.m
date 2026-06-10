function fig = box_notched()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    data = randn(200, 4) + [0 0.5 1.5 1];
    fig = figure;
    boxplot(data, 'Labels', {'A','B','C','D'}, 'Notch','on');
    ylabel('value'); title('Notched box'); grid on;
end
