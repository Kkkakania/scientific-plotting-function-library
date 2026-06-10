function fig = clarke_transform()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 0.04, 500); w = 2*pi*50;
    a = sin(w*t); b = sin(w*t - 2*pi/3); c = sin(w*t + 2*pi/3);
    alpha = (2/3)*(a - 0.5*b - 0.5*c);
    beta  = (2/3)*(sqrt(3)/2*b - sqrt(3)/2*c);
    fig = figure('Position',[100 100 600 500]);
    plot(alpha, beta, 'Color', palette('cat',1), 'LineWidth', 1.5);
    xline(0,'Color',[0.6 0.6 0.6]); yline(0,'Color',[0.6 0.6 0.6]);
    xlabel('\alpha'); ylabel('\beta'); title('\alpha\beta trajectory');
    axis equal; grid on;
end
