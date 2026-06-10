function fig = ber_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    ebn0_db = linspace(0, 14, 30); ebn0 = 10.^(ebn0_db/10);
    bpsk  = 0.5*erfc(sqrt(ebn0));
    qam16 = (3/8)*erfc(sqrt((2/5)*ebn0));
    qam64 = (7/24)*erfc(sqrt((1/7)*ebn0));
    fig = figure;
    semilogy(ebn0_db, bpsk,  'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    semilogy(ebn0_db, bpsk,  '--', 'Color', palette('cat',2), 'LineWidth', 1.5);
    semilogy(ebn0_db, qam16, 'Color', palette('cat',3), 'LineWidth', 1.5);
    semilogy(ebn0_db, qam64, 'Color', palette('cat',4), 'LineWidth', 1.5);
    ylim([1e-6 1]); xlabel('E_b/N_0 (dB)'); ylabel('BER');
    title('BER vs E_b/N_0');
    legend({'BPSK','QPSK','16-QAM','64-QAM'}); grid on;
end
