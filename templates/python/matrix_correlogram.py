"""matrix_correlogram: 相关阵的气泡+颜色混合编码."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging

def make_figure(title='Correlogram'):
    apply_theme()
    rng = np.random.default_rng(15)
    X = rng.standard_normal((200, 7))
    X[:, 1] = 0.7*X[:, 0] + 0.3*X[:, 1]
    X[:, 3] = -0.5*X[:, 2] + 0.5*X[:, 3]
    M = np.corrcoef(X.T); n = M.shape[0]
    Y, X_idx = np.indices(M.shape)
    fig, ax = plt.subplots(figsize=(6, 6))
    sc = ax.scatter(X_idx.ravel(), Y.ravel(),
                    s=np.abs(M).ravel()*700, c=M.ravel(),
                    cmap=diverging(), vmin=-1, vmax=1,
                    edgecolors='w', linewidth=0.5)
    fig.colorbar(sc, ax=ax, label='r', shrink=0.8)
    names = [f'v{i+1}' for i in range(n)]
    ax.set_xticks(range(n)); ax.set_xticklabels(names)
    ax.set_yticks(range(n)); ax.set_yticklabels(names)
    ax.invert_yaxis(); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
