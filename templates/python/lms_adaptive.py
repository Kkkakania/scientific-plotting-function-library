"""lms_adaptive: LMS 自适应滤波收敛（权值轨迹 + 误差下降）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def lms(d, x, mu=0.05, order=8):
    """最小均方自适应滤波：返回误差 e 与权值历史 W (n×order)."""
    n = len(d)
    w = np.zeros(order)
    buf = np.zeros(order)
    e = np.zeros(n)
    W = np.zeros((n, order))
    for k in range(n):
        buf[1:] = buf[:-1]; buf[0] = x[k]
        e[k] = d[k] - w @ buf
        w += mu * e[k] * buf
        W[k] = w
    return e, W


def make_figure(n=2000, mu=0.05, noise=1e-2,
                title='LMS adaptive filter convergence'):
    apply_theme(fig_size=(6, 5))
    rng = np.random.default_rng(11)
    h_true = np.array([0.8, -0.5, 0.35, 0.2, -0.12, 0.08, -0.05, 0.03])
    order = len(h_true)
    x = rng.normal(0, 1, n)                       # 白噪声激励
    d = np.convolve(x, h_true)[:n] + rng.normal(0, noise, n)
    e, W = lms(d, x, mu=mu, order=order)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    k = np.arange(n)
    for i in range(order):
        ax1.plot(k, W[:, i], color=cycle(i), lw=1.0)
        ax1.axhline(h_true[i], color=cycle(i), lw=0.8, ls='--', alpha=0.5)
    ax1.set_xlim(0, n); ax1.set_xlabel('iteration')
    ax1.set_ylabel('weight value')
    ax1.set_title(f'weight trajectories vs true taps (order={order}, μ={mu})')
    ax1.grid(True, linestyle=':', alpha=0.5)

    sq_err = e ** 2
    win = 50
    smooth = np.convolve(sq_err, np.ones(win) / win, mode='same')
    ax2.semilogy(k, sq_err, color=cycle(7), lw=0.5, alpha=0.55,
                 label='instantaneous $e^2(n)$')
    ax2.semilogy(k, smooth, color=cycle(1), lw=1.5,
                 label=f'smoothed ({win}-pt)')
    ax2.axhline(noise ** 2, color=cycle(2), lw=1.0, ls='--',
                label='noise floor')
    ax2.set_xlim(0, n); ax2.set_xlabel('iteration')
    ax2.set_ylabel('squared error')
    ax2.set_title('learning curve')
    ax2.legend(frameon=False, fontsize=8)
    ax2.grid(True, linestyle=':', alpha=0.5)
    fig.suptitle(title)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
