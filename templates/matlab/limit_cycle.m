function fig = limit_cycle()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    mu = 1.5;
    vdp = @(t,s) [s(2); mu*(1 - s(1)^2)*s(2) - s(1)];
    fig = figure('Position',[100 100 600 500]); hold on;
    ics = {[0.1 0], [2.5 2.5], [-2.5 -1]};
    for k = 1:numel(ics)
        [~, sol] = ode45(vdp, [0 30], ics{k});
        plot(sol(:, 1), sol(:, 2), 'Color', palette('cat',k), 'LineWidth', 0.8);
    end
    axis equal; xlabel('x'); ylabel('y'); title('Van der Pol limit cycle'); grid on;
end
