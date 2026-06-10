function fig = decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    X = [randn(80,2); randn(80,2) + 3];
    y = [zeros(80,1); ones(80,1)];
    w = [X ones(size(X,1),1)] \ (y - 0.5);
    [XX, YY] = meshgrid(linspace(-3,6,200));
    score = w(1)*XX + w(2)*YY + w(3);
    fig = figure('Position',[100 100 600 500]);
    contourf(XX, YY, double(score > 0), [-0.5 0.5 1.5], 'LineStyle','none'); hold on;
    colormap([palette('cat',1)*0.3 + 0.7; palette('cat',2)*0.3 + 0.7]);
    contour(XX, YY, score, [0 0], 'k', 'LineWidth', 1.5);
    for k = 0:1
        m = y == k;
        scatter(X(m,1), X(m,2), 30, palette('cat',k+1), 'filled', 'MarkerEdgeColor','w');
    end
    xlabel('x'); ylabel('y'); title('Decision boundary');
    legend({'class 0 region','class 1 region','boundary','class 0','class 1'}); axis equal;
end
