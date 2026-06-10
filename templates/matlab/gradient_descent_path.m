function fig = gradient_descent_path()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    f = @(x, y) x.^2 + 5*y.^2;
    [X, Y] = meshgrid(linspace(-3,3,200), linspace(-2,2,200));
    Z = f(X, Y);
    fig = figure('Position',[100 100 700 500]);
    contour(X, Y, Z, 15); hold on;
    colormap(parula);
    lrs = [0.1 0.04 0.18]; labs = {'lr=0.1','lr=0.04','lr=0.18'};
    for i = 1:3
        lr = lrs(i); p = [-2.5; 1.8]; path = p';
        for k = 1:30
            p = p - lr * [2*p(1); 10*p(2)];
            path = [path; p'];
        end
        plot(path(:,1), path(:,2), '-o', 'Color', palette('cat',i), 'MarkerSize', 4);
    end
    scatter(0, 0, 120, 'r', 'p', 'filled');
    xlabel('x'); ylabel('y'); title('Gradient descent path');
    legend(labs); axis equal;
end
