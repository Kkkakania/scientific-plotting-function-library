function fig = kalman_tracking()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    n = 80; Q = 0.04; R = 4.0;            % 过程/观测噪声方差
    x_true = 27 + cumsum(sqrt(Q)*randn(1,n));
    z = x_true + sqrt(R)*randn(1,n);      % 含噪观测
    x_est = zeros(1,n); P = 1.0; x = z(1);
    for k = 1:n
        x_pred = x; P_pred = P + Q;       % 预测
        K = P_pred/(P_pred + R);          % 卡尔曼增益
        x = x_pred + K*(z(k) - x_pred);   % 更新
        P = (1 - K)*P_pred;
        x_est(k) = x;
    end
    t = 1:n;
    fig = figure;
    scatter(t, z, 14, palette('cat',8), 'filled', 'MarkerFaceAlpha', 0.6); hold on;
    plot(t, x_true, 'Color', palette('cat',3), 'LineWidth', 2);
    plot(t, x_est, 'Color', palette('cat',2), 'LineWidth', 1.8);
    xlabel('time step'); ylabel('state value'); title('Kalman filter tracking');
    legend({'measurement','true state','Kalman estimate'}, 'Box', 'off');
    grid on;
end
