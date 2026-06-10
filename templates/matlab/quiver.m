function fig = quiver_field()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-2,2,16));
    U = -Y; V = X;
    fig = figure;
    quiver(X, Y, U, V, 1.2, 'Color', palette('cat',1), 'LineWidth', 0.8);
    axis equal tight; xlabel('x'); ylabel('y'); title('Quiver field');
end
