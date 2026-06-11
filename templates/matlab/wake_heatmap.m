function fig = wake_heatmap()
    % Jensen (Park) 尾流模型俯视风速云图, 风沿 +x:
    % a = (1-sqrt(1-Ct))/(1+2k*x/D)^2, r_w = D/2 + k*x, 多机亏损 RSS 叠加
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    u0 = 10; ct = 0.8; k = 0.05; d = 80;
    % 8 台风机: 4 列 x 2 行交错布局 (5D 顺风距, 3D 横风距)
    tx = [0 5 10 15 0 5 10 15] * d;
    ty = ([0 0 0 0 3 3 3 3] + [0 0.5 0 0.5 0 0.5 0 0.5]) * d;
    x = linspace(-2*d, 20*d, 440); y = linspace(-2*d, 6*d, 180);
    [X, Y] = meshgrid(x, y);
    a_sq = zeros(size(X));
    for i = 1:numel(tx)
        dx = X - tx(i); dy = Y - ty(i);
        rw = d/2 + k*dx;
        inwake = (dx > 0) & (abs(dy) < rw);
        a = (1 - sqrt(1 - ct)) ./ (1 + 2*k*dx/d).^2;
        a_sq = a_sq + inwake .* a.^2;
    end
    U = u0 * (1 - sqrt(a_sq));
    fig = figure('Position', [100 100 700 340]);
    pcolor(X/d, Y/d, U); shading interp; hold on;
    colormap(flipud(palette('seq_blue'))); caxis([0.45*u0, u0]);
    cb = colorbar; cb.Label.String = 'wind speed (m/s)';
    hT = plot(tx/d, ty/d, 'o', 'MarkerSize', 7, 'MarkerFaceColor', 'w', ...
              'MarkerEdgeColor', 'k', 'LineWidth', 1.0);
    for i = 1:numel(tx)                                       % 转子线
        plot([tx(i) tx(i)]/d, ty(i)/d + [-0.5 0.5], 'k', 'LineWidth', 1.6);
    end
    annotation('textarrow', [0.14 0.20], [0.80 0.80], 'String', 'wind', ...
               'FontSize', 9);
    axis equal tight;
    xlabel('x / D'); ylabel('y / D');
    title('Wind farm wake map (Jensen model)');
    legend(hT, {'Turbine'}, 'Location', 'southeast', 'Box', 'off');
end
