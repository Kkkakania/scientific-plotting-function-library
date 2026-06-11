"""kalman_tracking: 一维卡尔曼滤波状态估计（真值/含噪观测/估计）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Kalman filter tracking'):
    apply_theme(fig_size=(7, 4))
    rng = np.random.default_rng(0)
    n = 80
    Q, R = 0.04, 4.0          # 过程噪声 / 观测噪声方差
    # 真值：缓慢漂移的常量 + 随机游走
    x_true = 27.0 + np.cumsum(np.sqrt(Q) * rng.standard_normal(n))
    z = x_true + np.sqrt(R) * rng.standard_normal(n)   # 含噪观测
    # 标量卡尔曼递推
    x_est = np.zeros(n); P = 1.0; x = z[0]
    for k in range(n):
        # 预测（A=1, B=0）
        x_pred = x; P_pred = P + Q
        # 更新
        K = P_pred / (P_pred + R)            # 卡尔曼增益
        x = x_pred + K * (z[k] - x_pred)
        P = (1 - K) * P_pred
        x_est[k] = x
    t = np.arange(n)
    fig, ax = plt.subplots()
    ax.scatter(t, z, s=14, color=cycle(7), alpha=0.6, label='measurement')
    ax.plot(t, x_true, color=cycle(2), lw=2, label='true state')
    ax.plot(t, x_est, color=cycle(1), lw=1.8, label='Kalman estimate')
    ax.set_xlabel('time step'); ax.set_ylabel('state value')
    ax.set_title(title); ax.legend(frameon=False)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
