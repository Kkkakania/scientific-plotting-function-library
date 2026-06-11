function fig = cube_heatmap()
%CUBE_HEATMAP 魔方热图：M*M*M 体素按值着色，留缝呈魔方状（单次 patch 向量化）
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    % demo 数据：4x4x4 标量场
    m = 4; s = 0.82;                       % s: 体素边长（<1 留缝）
    [ii, jj, kk] = ndgrid(0:m-1, 0:m-1, 0:m-1);
    data = sin(0.9*ii) + cos(0.7*jj) + 0.5*kk + 0.15*randn(m, m, m);

    % 单位立方体 8 角点与 6 面索引
    corners = [0 0 0; 1 0 0; 1 1 0; 0 1 0; 0 0 1; 1 0 1; 1 1 1; 0 1 1];
    faces0  = [1 2 3 4; 5 6 7 8; 1 2 6 5; 4 3 7 8; 2 3 7 6; 1 4 8 5];

    n = m^3;
    origin = [ii(:), jj(:), kk(:)];                       % n x 3
    % 顶点：每个体素 8 个角点 → (8n) x 3
    verts = kron(origin, ones(8, 1)) + repmat(s*corners, n, 1);
    % 面：每个体素 6 面，索引整体偏移 → (6n) x 4
    offs  = kron((0:n-1)'*8, ones(6, 1));
    faces = repmat(faces0, n, 1) + repmat(offs, 1, 4);
    % 每面颜色 = 体素值（标量 CData，配 colormap）
    cdat  = kron(data(:), ones(6, 1));

    fig = figure;
    patch('Vertices', verts, 'Faces', faces, ...
          'FaceVertexCData', cdat, 'FaceColor', 'flat', ...
          'EdgeColor', 'w', 'LineWidth', 0.3);
    colormap(palette('seq_blue'));
    cb = colorbar; cb.Label.String = 'value';
    view(3); axis equal vis3d;
    lim = [-0.2, m-1+s+0.2];
    xlim(lim); ylim(lim); zlim(lim);
    t = (0:m-1) + s/2;
    set(gca, 'XTick', t, 'YTick', t, 'ZTick', t, ...
        'XTickLabel', 0:m-1, 'YTickLabel', 0:m-1, 'ZTickLabel', 0:m-1, ...
        'Box', 'off');
    xlabel('i'); ylabel('j'); zlabel('k');
    title('Cube heatmap');
    grid on;
end
