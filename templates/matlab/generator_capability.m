function fig = generator_capability()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    S = 1.0; Xs = 1.6; E_max = 2.3; V = 1.0;
    th = linspace(0, pi, 300);
    fig = figure; hold on;
    plot(S*sin(th), S*cos(th), 'Color', palette('cat',1), 'DisplayName', 'armature limit');
    r_f = V*E_max/Xs; c_f = -V^2/Xs;
    Pf = r_f*sin(th); Qf = c_f + r_f*cos(th); m = Qf >= -0.05;
    plot(Pf(m), Qf(m), 'Color', palette('cat',2), 'DisplayName', 'field limit');
    yline(0, 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8, 'HandleVisibility', 'off');
    plot([0.95 0.95], [-0.35 1.05], '--', 'Color', palette('cat',3), 'DisplayName', 'turbine limit');
    plot([0 0.95], [-0.35 -0.35], '-.', 'Color', palette('cat',4), 'DisplayName', 'end-region heating');
    text(0.35, 0.25, sprintf('safe operating\nregion'), 'HorizontalAlignment', 'center');
    xlabel('P (p.u.)'); ylabel('Q (p.u.)');
    title('Synchronous generator capability curve');
    legend('Location', 'northeast', 'FontSize', 7); grid on;
    xlim([0 1.45]); ylim([-0.55 1.2]);
end
