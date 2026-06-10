"""potential_field: 标量势场的等势线 + 梯度箭头."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Potential + gradient'):
    apply_theme(fig_size=(6, 5))
    Y, X = np.mgrid[-3:3:120j, -3:3:120j]
    V = -1/np.sqrt((X-1)**2 + Y**2 + 0.05) + 1/np.sqrt((X+1)**2 + Y**2 + 0.05)
    Ey, Ex = np.gradient(-V)
    skip = (slice(None, None, 8), slice(None, None, 8))
    fig, ax = plt.subplots()
    cs = ax.contour(X, Y, V, levels=15, cmap='RdBu_r', linewidths=0.8)
    ax.clabel(cs, inline=True, fontsize=6, fmt='%.2f')
    ax.quiver(X[skip], Y[skip], Ex[skip], Ey[skip], color='k', alpha=0.6, scale=80)
    ax.set_aspect('equal'); ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
