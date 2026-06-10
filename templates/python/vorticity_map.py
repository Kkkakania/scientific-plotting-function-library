"""vorticity_map: 涡量场 ω = ∂v/∂x − ∂u/∂y."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Vorticity field'):
    apply_theme(fig_size=(7, 5))
    Y, X = np.mgrid[-2:2:200j, -2:2:200j]
    U = -Y * np.exp(-(X**2 + Y**2)/2)
    V =  X * np.exp(-(X**2 + Y**2)/2)
    dV_dx = np.gradient(V, axis=1)
    dU_dy = np.gradient(U, axis=0)
    omega = dV_dx - dU_dy
    fig, ax = plt.subplots()
    pc = ax.pcolormesh(X, Y, omega, cmap='RdBu_r', shading='auto')
    fig.colorbar(pc, ax=ax, label='ω')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
