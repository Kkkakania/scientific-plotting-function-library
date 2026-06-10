"""calibration_curve: 校准曲线（预测概率 vs 实际频率）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Calibration curve'):
    apply_theme()
    rng = np.random.default_rng(12)
    n = 2000
    p_true = rng.uniform(0, 1, n)
    y = (rng.uniform(0, 1, n) < p_true).astype(int)
    p_pred = p_true + rng.normal(0, 0.1, n); p_pred = np.clip(p_pred, 0, 1)
    bins = np.linspace(0, 1, 11)
    mids = (bins[:-1] + bins[1:]) / 2
    obs = np.zeros(10)
    for i in range(10):
        mask = (p_pred >= bins[i]) & (p_pred < bins[i+1])
        obs[i] = y[mask].mean() if mask.sum() > 0 else np.nan
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], '--', color='gray', linewidth=0.8, label='ideal')
    ax.plot(mids, obs, '-o', color=cycle(0), label='model')
    ax.set_xlabel('predicted probability'); ax.set_ylabel('observed frequency'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
