"""heatmap_annotated: 单元格内显示数值."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential
from demo_data import gen_matrix

def make_figure(M=None, title='Annotated heatmap'):
    apply_theme()
    if M is None:
        M = gen_matrix(rows=6, cols=8)
    fig, ax = plt.subplots()
    im = ax.imshow(M, cmap=sequential(hue='blue'), aspect='auto')
    fig.colorbar(im, ax=ax, label='value')
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            col = 'white' if M[i,j] > M.mean() else 'black'
            ax.text(j, i, f'{M[i,j]:.2f}', ha='center', va='center', color=col, fontsize=7)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
