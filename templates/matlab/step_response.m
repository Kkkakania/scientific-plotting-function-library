function fig = step_response()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 5, 500); wn = 2*pi;
    zetas = [0.1 0.3 0.707 1.5];
    fig = figure; hold on;
    for k = 1:numel(zetas)
        z = zetas(k);
        if z < 1
            wd = wn*sqrt(1 - z^2);
            y = 1 - exp(-z*wn*t).*(cos(wd*t) + z/sqrt(1-z^2)*sin(wd*t));
        elseif z == 1
            y = 1 - exp(-wn*t).*(1 + wn*t);
        else
            wd = wn*sqrt(z^2 - 1);
            y = 1 - exp(-z*wn*t).*(cosh(wd*t) + z/sqrt(z^2-1)*sinh(wd*t));
        end
        plot(t, y, 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    yline(1, '--', 'Color', [0.5 0.5 0.5]);
    xlabel('t'); ylabel('y(t)'); title('Step response');
    legend(arrayfun(@(z)sprintf('\\zeta=%.3g',z), zetas, 'UniformOutput', false));
    grid on;
end
