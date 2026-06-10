function fig = nichols_chart()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    w = logspace(-1, 2, 500); s = 1j*w;
    G = 10 ./ (s .* (s/5 + 1) .* (s/50 + 1));
    fig = figure('Position',[100 100 600 550]);
    plot(angle(G)*180/pi, 20*log10(abs(G)), 'Color', palette('cat',1), 'LineWidth', 1.5);
    yline(0,'Color',[0.5 0.5 0.5]); xline(-180,'Color',[0.5 0.5 0.5]);
    xlabel('phase (°)'); ylabel('|G| (dB)'); title('Nichols chart'); grid on;
end
