"""decision_boundary: 分类器决策边界（2D）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Decision boundary'):
    apply_theme(fig_size=(6, 5))
    rng = np.random.default_rng(6)
    X = np.vstack([rng.normal((0, 0), 1, (80, 2)),
                   rng.normal((3, 3), 1, (80, 2))])
    y = np.array([0]*80 + [1]*80)
    # 简单线性边界（最小二乘）
    w = np.linalg.lstsq(np.c_[X, np.ones(len(X))], y - 0.5, rcond=None)[0]
    XX, YY = np.meshgrid(np.linspace(-3, 6, 200), np.linspace(-3, 6, 200))
    score = w[0]*XX + w[1]*YY + w[2]
    pred = (score > 0).astype(float)
    fig, ax = plt.subplots()
    ax.contourf(XX, YY, pred, levels=[-0.5, 0.5, 1.5],
                colors=[cycle(0), cycle(1)], alpha=0.2)
    ax.contour(XX, YY, score, levels=[0], colors='k', linewidths=1.5)
    for k in [0, 1]:
        m = y == k
        ax.scatter(X[m, 0], X[m, 1], s=30, color=cycle(k),
                   edgecolors='w', linewidth=0.4, label=f'class {k}')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
