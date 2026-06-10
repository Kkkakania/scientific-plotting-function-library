function fig = feeder_voltage_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    node = 0:15;
    base = 1.0 - 0.0042*node - 0.00012*node.^2;
    dg = base; dg(9:end) = dg(9:end) + 0.0035*(node(9:end) - 7);
    fig = figure; hold on;
    plot(node, base, 'o-', 'Color', palette('cat',1), 'MarkerSize', 4, 'DisplayName', 'without DG');
    plot(node, dg, 's-', 'Color', palette('cat',2), 'MarkerSize', 4, 'DisplayName', 'with DG @ node 8');
    yline(0.95, '--', 'lower limit 0.95 p.u.', 'Color', palette('cat',4), 'HandleVisibility', 'off');
    xline(8, ':', 'Color', [0.6 0.6 0.6], 'HandleVisibility', 'off');
    xlabel('node number'); ylabel('voltage (p.u.)');
    title('Feeder voltage profile with/without DG'); legend; grid on;
end
