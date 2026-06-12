"""meta_funnel: Meta 分析漏斗图（效应量 vs 标准误 + 伪 95%/99% 置信漏斗）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(pooled=0.40, n_study=30, title='Funnel plot'):
    apply_theme()
    rng = np.random.default_rng(13)
    se = rng.uniform(0.04, 0.42, n_study)
    eff = pooled + se * rng.standard_normal(n_study)
    # 少量小样本研究带正向偏倚，制造轻微不对称
    bias = se > 0.3
    eff[bias] += 0.25 * se[bias]
    se_grid = np.linspace(0, 0.45, 100)
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    for z, ls, lbl in [(1.96, '--', '95% pseudo-CI'), (2.576, ':', '99% pseudo-CI')]:
        ax.plot(pooled - z*se_grid, se_grid, ls, color='gray', linewidth=0.9,
                label=lbl)
        ax.plot(pooled + z*se_grid, se_grid, ls, color='gray', linewidth=0.9)
    ax.fill_betweenx(se_grid, pooled - 1.96*se_grid, pooled + 1.96*se_grid,
                     color=cycle(0), alpha=0.08)
    ax.scatter(eff, se, s=30, color=cycle(0), alpha=0.75, edgecolors='w',
               linewidth=0.4, zorder=3)
    ax.axvline(pooled, color=cycle(1), linewidth=1.2,
               label=f'pooled effect = {pooled:.2f}')
    ax.set_ylim(0.45, 0)                                  # SE 轴倒置
    ax.set_xlabel('effect size (standardized mean difference)')
    ax.set_ylabel('standard error')
    ax.set_title(title)
    ax.legend(loc='lower left')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
