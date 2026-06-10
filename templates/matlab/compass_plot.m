function fig = compass_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(22);
    n = 8; theta = linspace(0, 2*pi, n+1); theta = theta(1:end-1);
    r = 0.4 + 0.6*rand(1, n);
    [u, v] = pol2cart(theta, r);
    fig = figure('Position',[100 100 550 550]);
    compass(u, v); title('Compass');
end
