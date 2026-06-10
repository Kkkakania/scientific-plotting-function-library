function fig = polar_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat',1);
    theta = linspace(0, 2*pi, 500); r = 1 + 0.6*sin(5*theta);
    fig = figure('Position',[100 100 550 550]);
    polarplot(theta, r, 'Color', c, 'LineWidth', 1.5); hold on;
    polarplot([theta theta(1)], [r r(1)], 'Color', c);
    title('Polar curve');
end
