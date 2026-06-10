function fig = contour_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    [X, Y] = meshgrid(linspace(-3, 3, 80)); Z = peaks(X, Y);
    fig = figure('Position',[100 100 650 500]);
    contour3(X, Y, Z, 40); colormap(parula);
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D contour');
    view(30, 60);
end
