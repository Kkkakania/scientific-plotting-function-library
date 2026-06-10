function fig = window_compare()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    N = 512;
    wins = {ones(N,1), hann(N), hamming(N), blackman(N), kaiser(N, 14)};
    names = {'rect','hann','hamming','blackman','kaiser'};
    fig = figure('Position',[100 100 800 500]);
    subplot(1,2,1); hold on;
    for i = 1:5
        plot(wins{i}, 'Color', palette('cat',i), 'LineWidth', 1.2);
    end
    xlabel('sample'); ylabel('amplitude'); title('Time domain');
    legend(names, 'FontSize', 7); grid on;
    subplot(1,2,2); hold on;
    for i = 1:5
        W = abs(fft(wins{i}, 4096)); W = W / max(W);
        f = linspace(0, 0.5, numel(W)/2);
        plot(f, 20*log10(W(1:numel(W)/2) + 1e-12), 'Color', palette('cat',i), 'LineWidth', 1.2);
    end
    xlim([0 0.05]); ylim([-100 5]);
    xlabel('normalized freq'); ylabel('dB'); title('Magnitude');
    legend(names, 'FontSize', 7); grid on;
end
