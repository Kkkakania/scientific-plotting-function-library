function fig = contour_filled()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3, 3, 80));
    Z = peaks(X, Y);
    fig = figure;
    contourf(X, Y, Z, 20, 'LineStyle','none');
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'z';
    xlabel('x'); ylabel('y'); title('Filled contour');
end
