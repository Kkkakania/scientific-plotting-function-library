function fig = power_curve_analysis()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    alpha = 0.05;
    d = linspace(0.1, 1.2, 120);
    n = linspace(5, 100, 120);
    [D, N] = meshgrid(d, n);
    z_a = sqrt(2) * erfinv(2*(1 - alpha/2) - 1);     % norm ppf without toolbox
    nc = D .* sqrt(N / 2);                           % noncentrality, normal approx
    pw = normcdf_(nc - z_a) + normcdf_(-nc - z_a);
    fig = figure('Position',[100 100 580 440]);
    contourf(D, N, pw, linspace(0, 1, 21), 'LineColor', 'none'); hold on;
    colormap(palette('seq_blue'));
    cb = colorbar; ylabel(cb, 'statistical power');
    [C1, h1] = contour(D, N, pw, [0.5 0.9 0.95], 'LineColor', [0.5 0.5 0.5], ...
                       'LineWidth', 0.8);
    clabel(C1, h1, 'FontSize', 7);
    [C2, h2] = contour(D, N, pw, [0.8 0.8], 'LineColor', palette('cat',2), ...
                       'LineWidth', 1.6);
    clabel(C2, h2, 'FontSize', 8);
    xlabel('effect size (Cohen''s d)');
    ylabel('sample size per group');
    title('Power: two-sample t-test (per-group n)');
end

function p = normcdf_(x)
    p = 0.5 * (1 + erf(x / sqrt(2)));
end
