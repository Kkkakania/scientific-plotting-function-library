"""confusion_matrix: 分类混淆矩阵 + 行归一化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(M=None, labels=None, title='Confusion matrix'):
    apply_theme()
    if M is None:
        M = np.array([[42, 3, 1, 0],
                      [4, 38, 2, 1],
                      [1, 5, 36, 2],
                      [0, 2, 3, 40]])
        labels = ['A', 'B', 'C', 'D']
    Mn = M / M.sum(axis=1, keepdims=True)
    fig, ax = plt.subplots()
    im = ax.imshow(Mn, cmap=sequential(hue='blue'), aspect='auto', vmin=0, vmax=1)
    fig.colorbar(im, ax=ax, label='proportion')
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            col = 'white' if Mn[i,j] > 0.5 else 'black'
            ax.text(j, i, f'{M[i,j]}', ha='center', va='center', color=col, fontsize=9)
    if labels:
        ax.set_xticks(range(len(labels))); ax.set_xticklabels(labels)
        ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels)
    ax.set_xlabel('predicted'); ax.set_ylabel('true'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
