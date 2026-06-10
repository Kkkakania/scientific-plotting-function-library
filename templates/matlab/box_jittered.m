function fig = box_jittered()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    data = randn(30, 4) + [0 1 2 1.5];
    fig = figure;
    boxplot(data, 'Labels', {'A','B','C','D'}, 'Symbol',''); hold on;
    for i = 1:4
        x = i + 0.24*(rand(30,1) - 0.5);
        plot(x, data(:,i), 'o', 'Color', palette('cat',i), ...
             'MarkerFaceColor', palette('cat',i), 'MarkerSize', 4);
    end
    ylabel('value'); title('Box + jitter'); grid on;
end
