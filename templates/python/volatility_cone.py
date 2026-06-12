"""volatility_cone: 波动率锥（多窗口滚动波动率分位带 + 当前值）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Volatility cone'):
    apply_theme()
    rng = np.random.default_rng(15)
    n = 1000
    vol_state = 0.010 * np.exp(0.4 * np.sin(np.arange(n) / 80))
    r = rng.standard_normal(n) * vol_state
    windows = np.array([5, 10, 21, 42, 63, 126])
    qs = {q: [] for q in (0.0, 0.25, 0.5, 0.75, 1.0)}
    current = []
    for w in windows:
        c1 = np.convolve(r, np.ones(w) / w, mode='valid')
        c2 = np.convolve(r**2, np.ones(w) / w, mode='valid')
        vol = np.sqrt(np.maximum(c2 - c1**2, 0)) * np.sqrt(252) * 100
        for q in qs:
            qs[q].append(np.quantile(vol, q))
        current.append(vol[-1])
    fig, ax = plt.subplots()
    ax.fill_between(windows, qs[0.0], qs[1.0], color=cycle(0), alpha=0.15,
                    label='min-max')
    ax.fill_between(windows, qs[0.25], qs[0.75], color=cycle(0), alpha=0.35,
                    label='25-75%')
    ax.plot(windows, qs[0.5], '-o', color=cycle(0), markersize=4,
            label='median')
    ax.plot(windows, current, 's--', color=cycle(1), markersize=5,
            label='current')
    ax.set_xscale('log'); ax.set_xticks(windows)
    ax.set_xticklabels(windows)
    ax.set_xlabel('window length (days)')
    ax.set_ylabel('annualized volatility (%)')
    ax.set_title(title)
    ax.legend(frameon=False)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
