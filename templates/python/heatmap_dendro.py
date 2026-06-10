"""heatmap_dendro: 热力图 + 侧边树状图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
from theme import apply_theme
from palette import diverging
from demo_data import gen_matrix

def make_figure(title='Heatmap + dendrogram'):
    apply_theme(fig_size=(7, 6))
    M = gen_matrix(rows=20, cols=15, kind='block')
    Zr = linkage(M,   method='ward'); ro = leaves_list(Zr)
    Zc = linkage(M.T, method='ward'); co = leaves_list(Zc)
    M_ord = M[np.ix_(ro, co)]
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 4], height_ratios=[1, 4], hspace=0.02, wspace=0.02)
    ax_top  = fig.add_subplot(gs[0, 1]); dendrogram(Zc, ax=ax_top,  no_labels=True, color_threshold=0); ax_top.axis('off')
    ax_left = fig.add_subplot(gs[1, 0]); dendrogram(Zr, ax=ax_left, orientation='left', no_labels=True, color_threshold=0); ax_left.axis('off')
    ax_main = fig.add_subplot(gs[1, 1])
    im = ax_main.imshow(M_ord, cmap=diverging(), aspect='auto')
    ax_main.set_xticks([]); ax_main.set_yticks([])
    fig.colorbar(im, ax=ax_main, shrink=0.7, pad=0.02)
    fig.suptitle(title)
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
