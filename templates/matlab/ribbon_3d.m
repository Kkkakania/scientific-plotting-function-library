function fig = ribbon_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 10, 80)';
    Y = zeros(numel(x), 5);
    for i = 1:5
        Y(:, i) = sin(x + (i-1)*0.6) .* exp(-x/8);
    end
    fig = figure('Position',[100 100 650 500]);
    h = ribbon(x, Y);
    for k = 1:numel(h), h(k).FaceColor = palette('cat', k); h(k).EdgeColor = 'none'; end
    xlabel('series'); ylabel('x'); zlabel('value'); title('3D ribbons');
    view(45, 30);
end
