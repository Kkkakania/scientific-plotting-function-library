function fig = iv_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    V = linspace(0, 22, 300);
    fig = figure('Position',[100 100 700 500]);
    yyaxis left;
    Gs = [1000 800 600 400];
    leglab = cell(1, numel(Gs));
    for k = 1:numel(Gs)
        G = Gs(k); Isc = 8.2*G/1000; Voc = 22 - 0.4*(1 - G/1000);
        I = Isc * (1 - exp((V - Voc)/2)); I(I < 0) = 0; I(I > Isc) = Isc;
        plot(V, I, 'Color', palette('cat',k), 'LineWidth', 1.5); hold on;
        leglab{k} = sprintf('G=%d', G);
    end
    ylabel('I (A)');
    yyaxis right;
    for k = 1:numel(Gs)
        G = Gs(k); Isc = 8.2*G/1000; Voc = 22 - 0.4*(1 - G/1000);
        I = Isc * (1 - exp((V - Voc)/2)); I(I < 0) = 0; I(I > Isc) = Isc;
        plot(V, V.*I, '--', 'Color', palette('cat',k));
    end
    ylabel('P (W)'); xlabel('V');
    title('PV I-V & P-V curves'); legend(leglab); grid on;
end
