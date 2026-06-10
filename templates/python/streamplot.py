"""streamplot: 流线图（连续矢量场的视觉化）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Streamlines'):
    apply_theme()
    Y, X = np.mgrid[-3:3:200j, -3:3:200j]
    U = -1 - X**2 + Y; V = 1 + X - Y**2
    mag = np.hypot(U, V)
    fig, ax = plt.subplots()
    ax.streamplot(X, Y, U, V, color=mag, cmap='plasma', linewidth=1, density=1.4)
    ax.set_aspect('equal')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
