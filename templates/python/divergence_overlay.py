"""divergence_overlay: 矢量场散度上色 + 流线叠加."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging

def make_figure(title='Divergence + streamlines'):
    apply_theme(fig_size=(6, 5))
    Y, X = np.mgrid[-3:3:200j, -3:3:200j]
    U = X + Y; V = X - Y
    div = np.gradient(U, axis=1) + np.gradient(V, axis=0)
    fig, ax = plt.subplots()
    pc = ax.pcolormesh(X, Y, div, cmap=diverging(), shading='auto')
    ax.streamplot(X, Y, U, V, color='k', linewidth=0.6, density=1.0)
    fig.colorbar(pc, ax=ax, label='divergence')
    ax.set_aspect('equal'); ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
