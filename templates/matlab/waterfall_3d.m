function fig = waterfall_3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(3);
    % 合成一族随参数演化的双峰谱线
    n_curves = 12; n_pts = 160;
    x = linspace(0, 10, n_pts);
    Z = zeros(n_curves, n_pts);
    for i = 1:n_curves
        c1 = 3.0 + 0.20*(i-1); c2 = 7.0 - 0.12*(i-1);
        a1 = 1.0 - 0.05*(i-1); a2 = 0.3 + 0.06*(i-1);
        Z(i, :) = a1*exp(-(x - c1).^2 / 0.5) ...
                + a2*exp(-(x - c2).^2 / 0.9) ...
                + 0.02*rand(1, n_pts);
    end
    [X, Y] = meshgrid(x, 0:n_curves-1);

    fig = figure;
    w = waterfall(X, Y, Z);
    set(w, 'LineWidth', 1.2);
    colormap(palette('seq_blue', 256));
    xlabel('frequency'); ylabel('series index'); zlabel('amplitude');
    title('Waterfall plot');
    view(-35, 35);
    grid on;
end
