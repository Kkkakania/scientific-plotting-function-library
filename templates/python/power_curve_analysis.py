"""power_curve_analysis: 统计功效等高线（效应量 × 每组样本量 → 双样本 t 检验功效）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from theme import apply_theme
from palette import sequential

def make_figure(alpha=0.05, title='Power: two-sample t-test (per-group n)'):
    apply_theme()
    d = np.linspace(0.1, 1.2, 120)
    n = np.linspace(5, 100, 120)
    D, N = np.meshgrid(d, n)
    z_a = stats.norm.ppf(1 - alpha / 2)
    nc = D * np.sqrt(N / 2)                  # 非中心参数（正态近似）
    power = stats.norm.cdf(nc - z_a) + stats.norm.cdf(-nc - z_a)
    fig, ax = plt.subplots(figsize=(5.8, 4.4))
    cf = ax.contourf(D, N, power, levels=np.linspace(0, 1, 21),
                     cmap=sequential('blue'))
    cs = ax.contour(D, N, power, levels=[0.5, 0.9, 0.95],
                    colors='gray', linewidths=0.8)
    ax.clabel(cs, fmt='%.2f', fontsize=7)
    c80 = ax.contour(D, N, power, levels=[0.8], colors=['#D55E00'],
                     linewidths=1.6)
    ax.clabel(c80, fmt='power = %.1f', fontsize=8)
    fig.colorbar(cf, ax=ax, label='statistical power')
    ax.set_xlabel("effect size (Cohen's d)")
    ax.set_ylabel('sample size per group')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
