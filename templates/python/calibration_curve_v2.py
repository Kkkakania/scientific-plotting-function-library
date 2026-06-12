"""calibration_curve_v2: 概率校准曲线（可靠性图 + 预测概率直方图副面板）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _reliability(y, p, n_bins=10):
    edges = np.linspace(0, 1, n_bins + 1)
    idx = np.clip(np.digitize(p, edges) - 1, 0, n_bins - 1)
    mids, obs = [], []
    for b in range(n_bins):
        m = idx == b
        if m.sum() >= 5:
            mids.append(p[m].mean()); obs.append(y[m].mean())
    return np.array(mids), np.array(obs)

def make_figure(title='Calibration (reliability) diagram'):
    apply_theme()
    rng = np.random.default_rng(21)
    n = 3000
    p_true = rng.beta(2, 2, n)
    y = (rng.uniform(0, 1, n) < p_true).astype(float)
    p_good = np.clip(p_true + rng.normal(0, 0.06, n), 0.001, 0.999)
    z = np.log(p_true / (1 - p_true)) * 1.8            # over-confident model
    p_over = 1 / (1 + np.exp(-z))
    fig, (ax, axh) = plt.subplots(2, 1, figsize=(5, 5.6), sharex=True,
                                  gridspec_kw={'height_ratios': [3, 1]})
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.8, label='perfect')
    for i, (p, name) in enumerate([(p_good, 'calibrated'), (p_over, 'over-confident')]):
        mids, obs = _reliability(y, p)
        ax.plot(mids, obs, '-o', color=cycle(i), markersize=4, label=name)
    ax.set_ylabel('observed frequency'); ax.set_title(title)
    ax.legend(loc='upper left'); ax.grid(True, linestyle=':', alpha=0.5)
    axh.hist([p_good, p_over], bins=20, color=[cycle(0), cycle(1)], alpha=0.8)
    axh.set_xlabel('predicted probability'); axh.set_ylabel('count')
    axh.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
