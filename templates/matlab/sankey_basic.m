function fig = sankey_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fig = figure('Position',[100 100 700 500]); hold on;
    sources = {'A','B','C'}; targets = {'X','Y','Z'};
    flows = [3 2 1; 2 3 2; 1 1 3];
    src_y = cumsum([0 sum(flows,2)']);
    tgt_y = cumsum([0 sum(flows,1)]);
    for i = 1:3
        for j = 1:3
            c = palette('cat', i);
            sy = src_y(i) + sum(flows(i,1:j-1));
            ty = tgt_y(j) + sum(flows(1:i-1,j));
            patch([0 1 1 0], [sy sy ty+flows(i,j) ty]+[0 0 -flows(i,j) -flows(i,j)], ...
                  c, 'FaceAlpha', 0.5, 'EdgeColor','none');
            patch([0 1 1 0], [sy sy+flows(i,j) sy+flows(i,j) sy], c, ...
                  'EdgeColor','none', 'FaceAlpha', 0);
        end
    end
    for i = 1:3
        patch([-0.05 0 0 -0.05], [src_y(i) src_y(i) src_y(i+1) src_y(i+1)], ...
              palette('cat',i), 'EdgeColor','none');
        text(-0.1, (src_y(i)+src_y(i+1))/2, sources{i}, 'HorizontalAlignment','right');
    end
    for j = 1:3
        patch([1 1.05 1.05 1], [tgt_y(j) tgt_y(j) tgt_y(j+1) tgt_y(j+1)], ...
              [0.5 0.5 0.5], 'EdgeColor','none');
        text(1.1, (tgt_y(j)+tgt_y(j+1))/2, targets{j});
    end
    axis off; title('Sankey'); xlim([-0.3 1.4]);
end
