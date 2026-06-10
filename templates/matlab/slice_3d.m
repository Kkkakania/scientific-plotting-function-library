function fig = slice_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    n = 30;
    [X, Y, Z] = meshgrid(linspace(-2, 2, n));
    V = exp(-(X.^2 + Y.^2 + Z.^2)/2);
    fig = figure('Position',[100 100 650 500]);
    slice(X, Y, Z, V, 0, 0, 0); shading interp;
    colormap(hot); colorbar;
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D slices');
    view(40, 30);
end
