"""velocity_field_cfd: 二维流场速度矢量 + 速度模值底色（CFD 风格）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Velocity field'):
    apply_theme(fig_size=(7, 5))
    Y, X = np.mgrid[-1:1:40j, -2:2:60j]
    U = 1 - X**2 + 0.3*Y          # 类 Poiseuille
    V = -0.15*Y*X
    speed = np.hypot(U, V)
    fig, ax = plt.subplots()
    pc = ax.pcolormesh(X, Y, speed, cmap='viridis', shading='auto')
    skip = (slice(None, None, 4), slice(None, None, 4))
    ax.quiver(X[skip], Y[skip], U[skip], V[skip], color='white', scale=25)
    fig.colorbar(pc, ax=ax, label='|U|')
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_title(title); ax.set_aspect('equal')
    fig.tight_layout(); return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
