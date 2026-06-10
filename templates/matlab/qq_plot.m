function fig = qq_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(5);
    fig = figure;
    qqplot(randn(300, 1));
    title('Q-Q plot vs Normal'); grid on;
end
