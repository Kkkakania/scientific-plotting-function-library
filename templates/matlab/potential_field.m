function fig = potential_field()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3,3,120));
    V = -1./sqrt((X-1).^2 + Y.^2 + 0.05) + 1./sqrt((X+1).^2 + Y.^2 + 0.05);
    [Vy, Vx] = gradient(-V);
    fig = figure('Position',[100 100 600 500]);
    [C, h] = contour(X, Y, V, 15); colormap(palette('div')); hold on;
    clabel(C, h, 'FontSize', 6);
    skip = 1:8:size(X,1);
    quiver(X(skip,skip), Y(skip,skip), Vx(skip,skip), Vy(skip,skip), ...
           'Color', 'k', 'AutoScaleFactor', 0.8);
    axis equal tight; xlabel('x'); ylabel('y'); title('Potential + gradient');
end
