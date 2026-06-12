"""bland_altman_v2: Bland-Altman 一致性图（差值 vs 均值 + ±1.96SD 界限及其置信区间带）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(m1=None, m2=None, title='Bland-Altman agreement'):
    apply_theme()
    if m1 is None:
        rng = np.random.default_rng(7)
        true = rng.uniform(30, 120, 100)
        m1 = true + rng.normal(0, 3.0, 100)
        m2 = true + 1.5 + rng.normal(0, 3.0, 100)
    mean = (m1 + m2) / 2
    diff = m1 - m2
    n = len(diff)
    md, sd = diff.mean(), diff.std(ddof=1)
    loa_lo, loa_hi = md - 1.96*sd, md + 1.96*sd
    se_md = sd / np.sqrt(n)                 # SE of mean bias
    se_loa = sd * np.sqrt(3.0 / n)          # approx SE of limits of agreement
    fig, ax = plt.subplots()
    xs = np.array([mean.min(), mean.max()])
    for c, se in [(md, se_md), (loa_lo, se_loa), (loa_hi, se_loa)]:
        ax.fill_between(xs, c - 1.96*se, c + 1.96*se, color=cycle(1), alpha=0.15, linewidth=0)
    ax.scatter(mean, diff, s=28, color=cycle(0), alpha=0.7, edgecolors='w', linewidth=0.4)
    ax.axhline(md, color=cycle(1), linewidth=1.2, label=f'bias = {md:.2f}')
    ax.axhline(loa_hi, color='gray', linestyle='--', linewidth=1, label=f'+1.96 SD = {loa_hi:.2f}')
    ax.axhline(loa_lo, color='gray', linestyle='--', linewidth=1, label=f'-1.96 SD = {loa_lo:.2f}')
    ax.set_xlabel('mean of two methods')
    ax.set_ylabel('difference (method 1 - method 2)')
    ax.set_title(title)
    ax.legend(loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
