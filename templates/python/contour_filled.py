"""contour_filled: 填充等高线."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging
from demo_data import gen_3d_surface

def make_figure(X=None, Y=None, Z=None, levels=20, title='Filled contour'):
    apply_theme()
    if X is None:
        X, Y, Z = gen_3d_surface(n=80)
    fig, ax = plt.subplots()
    cf = ax.contourf(X, Y, Z, levels=levels, cmap=diverging())
    fig.colorbar(cf, ax=ax, label='z')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
