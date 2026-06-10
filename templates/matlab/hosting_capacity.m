function fig = hosting_capacity()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    groups = {'urban short', 'urban long', 'suburban', 'rural short', 'rural long'};
    centers = [6.5 4.8 3.6 2.4 1.5];
    fig = figure; hold on;
    data = cell(1, 5);
    for i = 1:5
        data{i} = max(centers(i) + centers(i)*0.22*randn(60, 1), 0.2);
        c = palette('cat', i);
        scatter(i + 0.06*randn(60, 1), data{i}, 7, c, 'filled', 'MarkerFaceAlpha', 0.5);
    end
    allv = cell2mat(data(:)')';
    grp = repelem(1:5, 60);
    boxplot(allv(:), grp(:), 'Labels', groups, 'Widths', 0.55, 'Symbol', '');
    ylabel('hosting capacity (MW)'); title('PV hosting capacity by feeder type');
    grid on;
end
