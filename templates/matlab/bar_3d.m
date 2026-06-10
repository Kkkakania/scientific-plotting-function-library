function fig = bar_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    M = 1 + 7*rand(5, 6);
    fig = figure('Position',[100 100 650 500]);
    b = bar3(M);
    for k = 1:numel(b), b(k).FaceColor = palette('cat', k); end
    xlabel('column'); ylabel('row'); zlabel('value'); title('3D bar');
end
