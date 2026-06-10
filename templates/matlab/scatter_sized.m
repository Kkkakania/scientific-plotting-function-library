function fig = scatter_sized()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    x = 10*rand(50,1); y = 10*rand(50,1); s = 20 + 400*rand(50,1);
    fig = figure;
    scatter(x, y, s, palette('cat',3), 'filled', 'MarkerFaceAlpha', 0.5, 'MarkerEdgeColor','k');
    xlabel('x'); ylabel('y'); title('Bubble chart'); grid on;
end
