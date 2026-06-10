"""correlation_matrix: 变量间相关系数矩阵."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging

def make_figure(M=None, names=None, title='Correlation matrix'):
    apply_theme()
    if M is None:
        rng = np.random.default_rng(0)
        X = rng.standard_normal((200, 6))
        X[:,1] = 0.7*X[:,0] + 0.3*X[:,1]
        X[:,3] = -0.5*X[:,2] + 0.5*X[:,3]
        M = np.corrcoef(X.T)
        names = [f'v{i+1}' for i in range(6)]
    fig, ax = plt.subplots()
    im = ax.imshow(M, cmap=diverging(), vmin=-1, vmax=1, aspect='auto')
    fig.colorbar(im, ax=ax, label='r')
    n = M.shape[0]
    for i in range(n):
        for j in range(n):
            ax.text(j, i, f'{M[i,j]:.2f}', ha='center', va='center', fontsize=7,
                    color='white' if abs(M[i,j]) > 0.6 else 'black')
    if names:
        ax.set_xticks(range(n)); ax.set_xticklabels(names)
        ax.set_yticks(range(n)); ax.set_yticklabels(names)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
