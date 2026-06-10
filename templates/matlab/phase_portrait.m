function fig = phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3, 3, 30));
    U = Y; V = -sin(X) - 0.2*Y;
    [sx, sy] = meshgrid(linspace(-3, 3, 8));
    fig = figure('Position',[100 100 600 500]);
    hl = streamline(X, Y, U, V, sx, sy);
    set(hl, 'Color', palette('cat',1), 'LineWidth', 0.8);
    axis equal tight;
    xlabel('x'); ylabel('dx/dt'); title('Phase portrait'); grid on;
end
