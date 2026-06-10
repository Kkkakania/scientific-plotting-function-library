function fig = errorbar_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0); c = palette('cat',1);
    x = 1:10; y = 2 + log(x) + 0.1*randn(1,10); err = 0.1 + 0.2*rand(1,10);
    fig = figure;
    errorbar(x, y, err, 'o-', 'Color', c, 'MarkerFaceColor', c, ...
             'LineWidth', 1.5, 'CapSize', 6);
    xlabel('x'); ylabel('y'); title('Errorbar'); grid on;
end
