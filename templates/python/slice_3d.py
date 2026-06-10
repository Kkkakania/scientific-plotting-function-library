"""slice_3d: 体积数据的切片可视化."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='3D slices'):
    apply_theme(fig_size=(6.5, 5))
    n = 30
    x, y, z = np.linspace(-2, 2, n), np.linspace(-2, 2, n), np.linspace(-2, 2, n)
    X, Y, Z = np.meshgrid(x, y, z)
    V = np.exp(-(X**2 + Y**2 + Z**2)/2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # 三个切片
    mid = n // 2
    for plane, idx in [('xy', mid), ('xz', mid), ('yz', mid)]:
        if plane == 'xy':
            ax.contourf(X[:, :, idx], Y[:, :, idx], V[:, :, idx], zdir='z', offset=z[idx], cmap='plasma', alpha=0.7)
        elif plane == 'xz':
            ax.contourf(X[:, idx, :], V[:, idx, :], Z[:, idx, :], zdir='y', offset=y[idx], cmap='plasma', alpha=0.7)
        else:
            ax.contourf(V[idx, :, :], Y[idx, :, :], Z[idx, :, :], zdir='x', offset=x[idx], cmap='plasma', alpha=0.7)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_zlim(-2, 2)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
