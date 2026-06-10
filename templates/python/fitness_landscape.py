"""fitness_landscape: 适应度地形（多峰函数等高线 + 个体位置）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Fitness landscape'):
    apply_theme(fig_size=(7, 5))
    X, Y = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-3, 3, 200))
    Z = -(np.sin(np.sqrt(X**2 + Y**2))**2 + 0.5*(X**2 + Y**2))
    rng = np.random.default_rng(3)
    pop = rng.uniform(-2.5, 2.5, (40, 2))
    fig, ax = plt.subplots()
    cf = ax.contourf(X, Y, Z, levels=20, cmap='terrain')
    ax.contour(X, Y, Z, levels=10, colors='k', linewidths=0.4, alpha=0.4)
    ax.scatter(pop[:, 0], pop[:, 1], s=30, c='red', edgecolors='white', linewidth=0.6, label='population')
    fig.colorbar(cf, ax=ax, label='fitness')
    ax.set_xlabel('x₁'); ax.set_ylabel('x₂'); ax.set_title(title)
    ax.legend(); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
