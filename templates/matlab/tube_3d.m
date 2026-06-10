function fig = tube_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 6*pi, 100);
    x = cos(t); y = sin(t); z = t/(2*pi);
    fig = figure('Position',[100 100 650 500]); hold on;
    for i = 1:numel(t)-1
        plot3(x(i:i+1), y(i:i+1), z(i:i+1), 'Color', parula_color(i/numel(t)), 'LineWidth', 3);
    end
    xlabel('x'); ylabel('y'); zlabel('z'); title('3D tube (helix)');
    view(45, 30); grid on;
end

function c = parula_color(v)
    cm = parula(256); idx = max(1, round(v*256));
    c = cm(idx, :);
end
