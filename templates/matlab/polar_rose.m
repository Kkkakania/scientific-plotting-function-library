function fig = polar_rose()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 16; theta = linspace(0, 2*pi, n+1); theta = theta(1:end-1);
    r = 0.3 + 0.7*rand(1, n);
    fig = figure('Position',[100 100 550 550]);
    polarhistogram('BinEdges', linspace(0, 2*pi, n+1), 'BinCounts', r, ...
                   'FaceColor', palette('cat',1), 'EdgeColor','w');
    title('Rose plot');
end
