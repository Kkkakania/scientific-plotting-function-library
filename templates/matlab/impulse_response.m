function fig = impulse_response()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 5, 500); wn = 2*pi;
    zetas = [0.1 0.3 0.707 1.5];
    fig = figure; hold on;
    for k = 1:numel(zetas)
        z = zetas(k);
        if z < 1
            wd = wn*sqrt(1-z^2);
            h = (wn/sqrt(1-z^2)) * exp(-z*wn*t) .* sin(wd*t);
        elseif z == 1
            h = wn^2 * t .* exp(-wn*t);
        else
            wd = wn*sqrt(z^2-1);
            h = (wn/sqrt(z^2-1)) * exp(-z*wn*t) .* sinh(wd*t);
        end
        plot(t, h, 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    yline(0, 'Color', [0.5 0.5 0.5]);
    xlabel('t'); ylabel('h(t)'); title('Impulse response');
    legend(arrayfun(@(z)sprintf('\\zeta=%.3g',z),zetas,'UniformOutput',false));
    grid on;
end
