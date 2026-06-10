function fig = pole_zero()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    zeros_ = [0.6+0.4j, 0.6-0.4j];
    poles  = [-0.5+0.3j, -0.5-0.3j, 0.2];
    theta = linspace(0, 2*pi, 200);
    fig = figure('Position',[100 100 550 550]);
    plot(cos(theta), sin(theta), 'k', 'LineWidth', 0.8); hold on;
    xline(0, 'Color', [0.6 0.6 0.6]); yline(0, 'Color', [0.6 0.6 0.6]);
    plot(real(zeros_), imag(zeros_), 'o', 'MarkerSize', 10, ...
         'MarkerFaceColor','none', 'MarkerEdgeColor', palette('cat',1), 'LineWidth', 1.6);
    plot(real(poles),  imag(poles),  'x', 'MarkerSize', 12, 'LineWidth', 1.8, ...
         'Color', palette('cat',2));
    axis equal; xlim([-1.5 1.5]); ylim([-1.5 1.5]);
    xlabel('Re'); ylabel('Im'); title('Pole-zero plot'); grid on;
end
