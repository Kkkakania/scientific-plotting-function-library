"""quiver: 矢量场箭头图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Quiver field'):
    apply_theme()
    X, Y = np.meshgrid(np.linspace(-2, 2, 16), np.linspace(-2, 2, 16))
    U = -Y; V = X
    mag = np.hypot(U, V)
    fig, ax = plt.subplots()
    ax.quiver(X, Y, U, V, mag, cmap='viridis', scale=25)
    ax.set_aspect('equal')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
