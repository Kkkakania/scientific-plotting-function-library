"""heatmap_basic: 基础热力图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential
from demo_data import gen_matrix

def make_figure(M=None, title='Heatmap'):
    apply_theme()
    if M is None:
        M = gen_matrix(rows=8, cols=12)
    fig, ax = plt.subplots()
    im = ax.imshow(M, cmap=sequential(hue='blue'), aspect='auto')
    fig.colorbar(im, ax=ax, label='value')
    ax.set_xlabel('column'); ax.set_ylabel('row'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
