"""contour_lines: 等值线（带标签）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from demo_data import gen_3d_surface

def make_figure(X=None, Y=None, Z=None, levels=12, title='Contour lines'):
    apply_theme()
    if X is None:
        X, Y, Z = gen_3d_surface(n=80)
    fig, ax = plt.subplots()
    cs = ax.contour(X, Y, Z, levels=levels, cmap='viridis', linewidths=1.0)
    ax.clabel(cs, inline=True, fontsize=7, fmt='%.2f')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
