function fig = population_pyramid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    n = 19;
    ages = arrayfun(@(i) sprintf('%d-%d', i*5, i*5+4), 0:n-2, 'UniformOutput', false);
    ages{end+1} = '90+';
    base = 4.2*exp(-(((0:n-1) - 6)/7.5).^2) + 0.4;
    male = base .* (1 + 0.16*(rand(1, n) - 0.5));
    female = base .* (1 + 0.16*(rand(1, n) - 0.5));
    female(end-3:end) = female(end-3:end)*1.25;
    y = 1:n;
    fig = figure; hold on;
    barh(y, -male, 'FaceColor', palette('cat', 1), 'EdgeColor', 'none', ...
         'DisplayName', 'male');
    barh(y, female, 'FaceColor', palette('cat', 2), 'EdgeColor', 'none', ...
         'DisplayName', 'female');
    xline(0, 'Color', [0.25 0.25 0.25], 'LineWidth', 0.8, 'HandleVisibility', 'off');
    yticks(y(1:2:end)); yticklabels(ages(1:2:end));
    mx = max([male female])*1.15; xlim([-mx mx]);
    xt = xticks; xticklabels(arrayfun(@(v) sprintf('%.0f', abs(v)), xt, 'UniformOutput', false));
    xlabel('population (%)'); ylabel('age group');
    title('Population pyramid'); legend; grid on;
    set(gca, 'FontSize', 8);
end
