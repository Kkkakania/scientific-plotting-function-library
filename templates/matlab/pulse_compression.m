function fig = pulse_compression()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    % LFM chirp 参数（时间带宽积 TBP = B*T = 100）
    T = 10e-6; B = 10e6; K = B / T;
    fs = 8 * B; n = round(fs * T);
    t = (-n/2:n/2-1) / fs;
    st = exp(1j*pi*K*t.^2);                 % LFM 信号
    ht = conj(fliplr(st));                  % 匹配滤波器
    % 匹配滤波输出（矩形窗 vs hamming 加窗）
    hamm = 0.54 - 0.46*cos(2*pi*(0:n-1)/(n-1));
    rect_db = todb(conv(st, ht));
    hamm_db = todb(conv(st .* hamm, ht));
    tau = ((0:2*n-2) - (n-1)) / fs * 1e6;   % 时延轴 (us)

    fig = figure;
    subplot(2,1,1);
    plot(t*1e6, real(st), 'Color', palette('cat',1), 'LineWidth', 0.8); hold on;
    plot(t*1e6, K*t/1e6/(B/2e6), 'Color', palette('cat',2), 'LineWidth', 1.2);
    xlabel('time (\mus)'); ylabel('amplitude');
    title(sprintf('LFM chirp, TBP = %.0f', B*T));
    legend({'Re s(t)', 'inst. freq (norm.)'}, 'Box', 'off', 'Location', 'northwest');
    grid on;

    subplot(2,1,2);
    plot(tau, rect_db, 'Color', palette('cat',1), 'LineWidth', 1); hold on;
    plot(tau, hamm_db, 'Color', palette('cat',2), 'LineWidth', 1);
    xlim([-1.5 1.5]); ylim([-80 3]);
    xlabel('delay (\mus)'); ylabel('output (dB)');
    title('Matched-filter output (pulse compression)');
    legend({'rectangular', 'hamming'}, 'Box', 'off');
    grid on;
end

function db = todb(x)
    mag = abs(x);
    db = 20*log10(mag / max(mag) + 1e-12);
end
