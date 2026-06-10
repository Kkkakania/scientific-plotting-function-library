function fig = star_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    n_obs = 6; n_var = 6;
    data = 0.3 + 0.7*rand(n_obs, n_var);
    ang = linspace(0, 2*pi, n_var+1);
    fig = figure('Position',[100 100 800 500]);
    for i = 1:n_obs
        subplot(2, 3, i);
        pax = polaraxes('Parent', gcf, 'Position', get(gca,'Position'));
        delete(gca);
        v = [data(i,:) data(i,1)];
        polarplot(pax, ang, v, 'Color', palette('cat',i), 'LineWidth', 1.5);
        pax.RTickLabel = {};
        title(pax, sprintf('obs %d', i));
    end
    sgtitle('Star plots');
end
