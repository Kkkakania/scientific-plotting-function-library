function fig = waffle_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    values = [35 25 20 12 8]; labels = {'A','B','C','D','E'};
    rows = 10; cols = 10; total = rows*cols;
    parts = round(values/sum(values) * total);
    parts(1) = parts(1) + total - sum(parts);
    flat = [];
    for i = 1:numel(parts), flat = [flat repmat(i, 1, parts(i))]; end
    flat = flat(1:total);
    grid = reshape(flat, rows, cols);
    fig = figure;
    for r = 1:rows
        for c = 1:cols
            rectangle('Position',[c-1, rows-r, 0.9, 0.9], ...
                      'FaceColor', palette('cat', grid(r,c)), 'EdgeColor','w');
        end
    end
    xlim([0 cols]); ylim([0 rows]); axis equal off;
    title('Waffle chart');
    h = zeros(1, numel(labels));
    for i = 1:numel(labels)
        h(i) = patch(NaN, NaN, palette('cat',i));
    end
    legend(h, arrayfun(@(i)sprintf('%s (%d%%)',labels{i},values(i)), ...
           1:numel(labels), 'UniformOutput', false), 'Location','eastoutside');
end
