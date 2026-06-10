"""pareto_front: 多目标优化 Pareto 前沿."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Pareto front'):
    apply_theme()
    rng = np.random.default_rng(2)
    n = 400
    f1 = rng.uniform(0, 1, n)
    f2 = (1 - f1**0.5) + 0.15*rng.uniform(0, 1, n)
    # 找非支配点
    pareto = np.ones(n, dtype=bool)
    for i in range(n):
        for j in range(n):
            if i != j and f1[j] <= f1[i] and f2[j] <= f2[i] and (f1[j] < f1[i] or f2[j] < f2[i]):
                pareto[i] = False; break
    fig, ax = plt.subplots()
    ax.scatter(f1[~pareto], f2[~pareto], s=15, c='lightgray', alpha=0.7, label='dominated')
    ax.scatter(f1[pareto],  f2[pareto],  s=30, c=cycle(1), label='Pareto front', edgecolors='k', linewidth=0.5)
    order = np.argsort(f1[pareto])
    ax.plot(f1[pareto][order], f2[pareto][order], color=cycle(1), linewidth=0.8)
    ax.set_xlabel('objective 1'); ax.set_ylabel('objective 2'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
