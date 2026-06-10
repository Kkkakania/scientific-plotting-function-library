function fig = residual_plot()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(10); c = palette('cat',1);
    x = 10*rand(80,1); y = 1.5*x + 2 + 1.5*randn(80,1);
    p = polyfit(x, y, 1); yhat = polyval(p, x); res = y - yhat;
    fig = figure;
    scatter(yhat, res, 30, c, 'filled', 'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w');
    yline(0, 'k');
    xlabel('predicted'); ylabel('residual'); title('Residual plot'); grid on;
end
