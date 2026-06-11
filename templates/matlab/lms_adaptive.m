function fig = lms_adaptive()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(11);
    % 系统辨识场景：白噪声激励未知 FIR，LMS 学习其抽头
    n = 2000; mu = 0.05; noise = 1e-2;
    h_true = [0.8 -0.5 0.35 0.2 -0.12 0.08 -0.05 0.03];
    order = numel(h_true);
    x = randn(1, n);
    d_full = conv(x, h_true);
    d = d_full(1:n) + noise*randn(1, n);
    % LMS 迭代（核心五行）
    w = zeros(order, 1); buf = zeros(order, 1);
    e = zeros(1, n); W = zeros(n, order);
    for k = 1:n
        buf = [x(k); buf(1:end-1)];
        e(k) = d(k) - w' * buf;
        w = w + mu * e(k) * buf;
        W(k, :) = w';
    end

    fig = figure;
    subplot(2,1,1); hold on;
    for i = 1:order
        c = palette('cat', i);
        plot(1:n, W(:, i), 'Color', c, 'LineWidth', 1);
        yline(h_true(i), '--', 'Color', c, 'Alpha', 0.5);
    end
    xlim([0 n]); xlabel('iteration'); ylabel('weight value');
    title(sprintf('Weight trajectories vs true taps (order=%d, \\mu=%.2f)', order, mu));
    grid on;

    subplot(2,1,2);
    sq = e.^2;
    sm = conv(sq, ones(1,50)/50, 'same');
    semilogy(1:n, sq, 'Color', [0.6 0.6 0.6 0.55], 'LineWidth', 0.5); hold on;
    semilogy(1:n, sm, 'Color', palette('cat',2), 'LineWidth', 1.5);
    yline(noise^2, '--', 'Color', palette('cat',3));
    xlim([0 n]); xlabel('iteration'); ylabel('squared error');
    title('Learning curve');
    legend({'instantaneous e^2(n)', 'smoothed (50-pt)', 'noise floor'}, 'Box', 'off');
    grid on;
end
