"""heatmap_clustered: 按行/列聚类排序后的热力图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list
from theme import apply_theme
from palette import diverging
from demo_data import gen_matrix

def make_figure(M=None, title='Clustered heatmap'):
    apply_theme()
    if M is None:
        M = gen_matrix(rows=20, cols=15, kind='block')
    row_order = leaves_list(linkage(M,   method='ward'))
    col_order = leaves_list(linkage(M.T, method='ward'))
    M_ord = M[np.ix_(row_order, col_order)]
    fig, ax = plt.subplots()
    im = ax.imshow(M_ord, cmap=diverging(), aspect='auto')
    fig.colorbar(im, ax=ax, label='value')
    ax.set_title(title); ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
