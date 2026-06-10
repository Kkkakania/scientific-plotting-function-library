function fig = capacity_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    snr_db = linspace(-10, 30, 200); snr = 10.^(snr_db/10);
    fig = figure;
    Bs = [1 5 20];
    hold on;
    for i = 1:numel(Bs)
        plot(snr_db, Bs(i)*log2(1 + snr), 'Color', palette('cat',i), 'LineWidth', 1.5);
    end
    xlabel('SNR (dB)'); ylabel('capacity (Mbit/s)'); title('Shannon capacity');
    legend(arrayfun(@(b)sprintf('B=%d MHz',b), Bs, 'UniformOutput',false));
    grid on;
end
