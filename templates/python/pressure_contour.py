"""pressure_contour: 压力场等高线（CFD 后处理常用）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Pressure contour'):
    apply_theme(fig_size=(7, 5))
    X, Y = np.meshgrid(np.linspace(-2, 4, 200), np.linspace(-2, 2, 100))
    # 圆柱绕流势流近似
    r2 = X**2 + Y**2 + 0.05
    P = 1 - (1 - (X**2 - Y**2)/r2**2)**2 - (2*X*Y/r2**2)**2
    fig, ax = plt.subplots()
    cf = ax.contourf(X, Y, P, levels=25, cmap='RdBu_r')
    cs = ax.contour(X, Y, P, levels=12, colors='k', linewidths=0.4)
    ax.clabel(cs, inline=True, fontsize=6, fmt='%.2f')
    ax.add_patch(plt.Circle((0, 0), 0.3, color='gray', zorder=5))
    fig.colorbar(cf, ax=ax, label='Cp')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
