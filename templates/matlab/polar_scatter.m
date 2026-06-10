function fig = polar_scatter()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(21);
    n = 200; theta = 2*pi*rand(n, 1);
    r = rand(n, 1) + 0.3*sin(3*theta);
    fig = figure('Position',[100 100 550 550]);
    polarscatter(theta, r, 25, r, 'filled', 'MarkerFaceAlpha', 0.7);
    colormap(parula); cb = colorbar; cb.Label.String = 'radius';
    title('Polar scatter');
end
