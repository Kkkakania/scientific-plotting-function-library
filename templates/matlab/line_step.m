function fig = line_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0); c = palette('cat', 1);
    x = 0:19; y = cumsum(randn(1, 20));
    fig = figure; stairs(x, y, 'Color', c, 'LineWidth', 1.5); hold on;
    plot(x, y, 'o', 'Color', c, 'MarkerFaceColor', c, 'MarkerSize', 4);
    xlabel('t'); ylabel('value'); title('Step plot'); grid on;
end
