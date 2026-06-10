function fig = histogram_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    fig = figure;
    histogram(randn(600,1), 30, 'FaceColor', palette('cat',1), 'EdgeColor','w');
    xlabel('value'); ylabel('count'); title('Histogram'); grid on;
end
