"""pacf_plot: 偏自相关图（AR(2) 合成序列，Durbin-Levinson 求 PACF + 置信带）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _pacf(y, nlags):
    y = y - y.mean()
    r = np.array([np.dot(y[:len(y)-k], y[k:]) for k in range(nlags + 1)])
    r = r / r[0]
    phi = np.zeros((nlags + 1, nlags + 1))
    phi[1, 1] = r[1]
    for k in range(2, nlags + 1):
        num = r[k] - np.dot(phi[k-1, 1:k], r[1:k][::-1])
        den = 1 - np.dot(phi[k-1, 1:k], r[1:k])
        phi[k, k] = num / den
        phi[k, 1:k] = phi[k-1, 1:k] - phi[k, k] * phi[k-1, 1:k][::-1]
    return np.array([phi[k, k] for k in range(1, nlags + 1)])

def make_figure(nlags=20, title='Partial autocorrelation (AR(2) demo)'):
    apply_theme()
    rng = np.random.default_rng(2)
    n = 400
    y = np.zeros(n)
    for i in range(2, n):
        y[i] = 0.6 * y[i-1] - 0.3 * y[i-2] + rng.standard_normal()
    pacf = _pacf(y, nlags)
    ci = 1.96 / np.sqrt(n)
    lags = np.arange(1, nlags + 1)
    fig, ax = plt.subplots()
    ax.axhspan(-ci, ci, color=cycle(0), alpha=0.15,
               label='95% confidence band')
    ax.axhline(0, color='#666666', linewidth=0.8)
    ax.vlines(lags, 0, pacf, color=cycle(0), linewidth=1.5)
    ax.plot(lags, pacf, 'o', color=cycle(1), markersize=4)
    ax.set_xlabel('lag'); ax.set_ylabel('partial autocorrelation')
    ax.set_title(title)
    ax.legend(frameon=False)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
