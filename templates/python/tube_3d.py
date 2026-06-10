"""tube_3d: 3D 螺旋管状（参数曲线渲染）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='3D tube (helix)'):
    apply_theme(fig_size=(6.5, 5))
    t = np.linspace(0, 6*np.pi, 100)
    x = np.cos(t); y = np.sin(t); z = t/(2*np.pi)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(t) - 1):
        ax.plot(x[i:i+2], y[i:i+2], z[i:i+2],
                color=plt.cm.viridis(i/len(t)), linewidth=3)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
