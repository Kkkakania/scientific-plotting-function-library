"""gradient_descent_path: 梯度下降路径在等高线上的可视化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Gradient descent path'):
    apply_theme(fig_size=(7, 5))
    f = lambda x, y: x**2 + 5*y**2
    grad = lambda x, y: np.array([2*x, 10*y])
    X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-2, 2, 200))
    Z = f(X, Y)
    fig, ax = plt.subplots()
    cs = ax.contour(X, Y, Z, levels=15, cmap='viridis', alpha=0.7)
    ax.clabel(cs, inline=True, fontsize=6, fmt='%.1f')
    for i, (lr, name) in enumerate([(0.1, 'lr=0.1'), (0.04, 'lr=0.04'), (0.18, 'lr=0.18')]):
        p = np.array([-2.5, 1.8]); path = [p.copy()]
        for _ in range(30):
            p = p - lr * grad(*p)
            path.append(p.copy())
        path = np.array(path)
        ax.plot(path[:, 0], path[:, 1], '-o', color=cycle(i), markersize=4, label=name)
    ax.scatter(0, 0, s=100, c='red', marker='*', zorder=5, label='optimum')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title)
    ax.legend(); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
