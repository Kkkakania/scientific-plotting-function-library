function fig = transformer_efficiency()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    P_fe = 0.01; P_cu = 0.02;
    k = linspace(0.02, 1.4, 400); pfs = [1.0 0.9 0.8];
    fig = figure; hold on;
    for i = 1:3
        pf = pfs(i);
        eta = k*pf./(k*pf + P_fe + k.^2*P_cu)*100;
        plot(k*100, eta, 'Color', palette('cat', i), 'DisplayName', sprintf('PF = %.1f', pf));
        kmax = sqrt(P_fe/P_cu);
        plot(kmax*100, kmax*pf/(kmax*pf + 2*P_fe)*100, 'o', 'Color', palette('cat', i), ...
             'MarkerSize', 4, 'HandleVisibility', 'off');
    end
    text(72, 95.4, '\eta_{max} at k = (P_{fe}/P_{cu})^{1/2}', 'FontSize', 8);
    xlabel('loading (%)'); ylabel('efficiency (%)');
    title('Transformer efficiency vs loading'); ylim([88 100]);
    legend('Location', 'southeast'); grid on;
end
