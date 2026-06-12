"""ewma_chart: EWMA 控制图（lambda=0.2，时变控制限，越限点标红）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(lam=0.2, L=3.0, title='EWMA control chart'):
    apply_theme()
    rng = np.random.default_rng(10)
    n, mu, sigma = 60, 50.0, 2.0
    x = rng.normal(mu, sigma, n)
    x[40:] += 1.2 * sigma                      # 注入漂移
    z = np.zeros(n); z[0] = mu
    for i in range(n):
        z[i] = lam * x[i] + (1 - lam) * (z[i-1] if i else mu)
    i1 = np.arange(1, n + 1)
    half = L * sigma * np.sqrt(lam / (2 - lam) * (1 - (1 - lam)**(2 * i1)))
    ucl, lcl = mu + half, mu - half
    t = np.arange(n)
    fig, ax = plt.subplots()
    ax.fill_between(t, lcl, ucl, color=cycle(0), alpha=0.10)
    ax.plot(t, x, '.', color=cycle(7), markersize=4, label='raw observation')
    ax.plot(t, z, '-o', color=cycle(0), markersize=3.5, label='EWMA')
    ax.plot(t, ucl, '--', color=cycle(7), linewidth=1, label='UCL / LCL')
    ax.plot(t, lcl, '--', color=cycle(7), linewidth=1)
    ax.axhline(mu, color=cycle(2), linewidth=1, label='target')
    out = (z > ucl) | (z < lcl)
    ax.plot(t[out], z[out], 'o', color=cycle(1), markersize=6,
            label='out of control')
    ax.set_xlabel('sample number'); ax.set_ylabel('value')
    ax.set_title(f'{title} ($\\lambda$={lam})')
    ax.legend(frameon=False, fontsize=7, loc='upper left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
