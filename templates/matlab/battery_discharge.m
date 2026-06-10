function fig = battery_discharge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    soc = linspace(100, 0, 200);
    Cs = [0.2 0.5 1.0 2.0];
    fig = figure;
    hold on;
    for k = 1:numel(Cs)
        C = Cs(k); plat = 3.7 - 0.05*C;
        V = plat - (100-soc)/100*0.5 - 0.15*C*exp(-soc/15);
        V(soc < 5) = V(soc < 5) - (5 - soc(soc < 5))*0.1;
        plot(100 - soc, V, 'Color', palette('cat',k), 'LineWidth', 1.5);
    end
    xlabel('capacity discharged (%)'); ylabel('voltage (V)');
    title('Battery discharge curves');
    legend(arrayfun(@(c)sprintf('%gC',c), Cs, 'UniformOutput', false));
    grid on;
end
