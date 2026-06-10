"""bland_altman: 两种测量方法的一致性分析."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(m1=None, m2=None, title='Bland-Altman'):
    apply_theme()
    if m1 is None:
        rng = np.random.default_rng(4)
        true = rng.uniform(20, 100, 80)
        m1 = true + rng.normal(0, 2, 80); m2 = true + rng.normal(0.5, 2, 80)
    mean = (m1 + m2) / 2; diff = m1 - m2
    md = diff.mean(); sd = diff.std()
    fig, ax = plt.subplots()
    ax.scatter(mean, diff, c=cycle(0), s=30, alpha=0.7, edgecolors='w', linewidth=0.4)
    ax.axhline(md,        color='k',  linestyle='-',  linewidth=1, label=f'mean = {md:.2f}')
    ax.axhline(md+1.96*sd, color='gray', linestyle='--', linewidth=1, label='+1.96 SD')
    ax.axhline(md-1.96*sd, color='gray', linestyle='--', linewidth=1, label='-1.96 SD')
    ax.set_xlabel('(M1 + M2) / 2'); ax.set_ylabel('M1 - M2'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
