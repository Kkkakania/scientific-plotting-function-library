function fig = network_architecture(sizes)
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    if nargin < 1, sizes = [4 6 6 3]; end
    apply_theme();
    fig = figure('Position',[100 100 800 500]); hold on;
    x_pos = linspace(0, 1, numel(sizes));
    coords = cell(numel(sizes), 1);
    for li = 1:numel(sizes)
        ys = linspace(0.1, 0.9, sizes(li));
        coords{li} = [x_pos(li)*ones(numel(ys),1) ys.'];
    end
    for i = 1:numel(sizes)-1
        for a = 1:sizes(i)
            for b = 1:sizes(i+1)
                plot([coords{i}(a,1) coords{i+1}(b,1)], ...
                     [coords{i}(a,2) coords{i+1}(b,2)], 'Color',[0.7 0.7 0.7], 'LineWidth', 0.3);
            end
        end
    end
    for li = 1:numel(sizes)
        for k = 1:sizes(li)
            rectangle('Position',[coords{li}(k,1)-0.025, coords{li}(k,2)-0.025, 0.05, 0.05], ...
                      'Curvature',[1 1], 'FaceColor', palette('cat',li), 'EdgeColor','none');
        end
        nm = sprintf('hidden %d', li-1);
        if li == 1, nm = 'input'; end
        if li == numel(sizes), nm = 'output'; end
        text(x_pos(li), 0.02, nm, 'HorizontalAlignment','center');
    end
    xlim([-0.05 1.05]); ylim([-0.02 1]); axis equal off; title('Network architecture');
end
