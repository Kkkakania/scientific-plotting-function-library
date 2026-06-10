function fig = line_collection_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    x = linspace(0, 10, 200);
    fig = figure('Position',[100 100 700 500]); hold on;
    cm = parula(8);
    for i = 1:8
        k = 0.5 + (i-1)*0.21;
        y = sin(k*x) .* exp(-x/8);
        plot3(x, i*ones(size(x)), y, 'Color', cm(i, :), 'LineWidth', 1.5);
    end
    xlabel('x'); ylabel('series'); zlabel('y');
    title('Stacked 3D curves'); view(30, -60); grid on;
end
