function fig = tree_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position',[100 100 800 500]);
    ax = axes; hold on;
    function node(x, y, txt, c)
        rectangle('Position', [x-0.25 y-0.25 0.5 0.5], 'Curvature', 1, 'FaceColor', c, 'EdgeColor', c);
        text(x, y, txt, 'HorizontalAlignment','center', 'Color','w', 'FontWeight','bold');
    end
    plot([4 2], [4 3], 'Color', [0.5 0.5 0.5]); plot([4 6], [4 3], 'Color', [0.5 0.5 0.5]);
    plot([2 1], [3 2], 'Color', [0.5 0.5 0.5]); plot([2 3], [3 2], 'Color', [0.5 0.5 0.5]);
    plot([6 5], [3 2], 'Color', [0.5 0.5 0.5]); plot([6 7], [3 2], 'Color', [0.5 0.5 0.5]);
    node(4, 4, 'X_1<0.5', palette('cat',1));
    node(2, 3, 'X_2<2', palette('cat',1));
    node(6, 3, 'X_2<3', palette('cat',1));
    node(1, 2, 'A', palette('cat',2));
    node(3, 2, 'B', palette('cat',3));
    node(5, 2, 'C', palette('cat',4));
    node(7, 2, 'D', palette('cat',5));
    xlim([0 8]); ylim([1.5 4.5]); axis equal off;
    title('Tree diagram');
end
