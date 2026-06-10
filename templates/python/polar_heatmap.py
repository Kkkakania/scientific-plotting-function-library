"""polar_heatmap: 极坐标连续热力图（如天线方向图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='Polar density'):
    apply_theme(fig_size=(5.5, 5.5))
    theta = np.linspace(0, 2*np.pi, 200)
    r = np.linspace(0, 1, 80)
    T, R = np.meshgrid(theta, r)
    Z = (1 + np.cos(4*T))*(1 - R**2)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    pc = ax.pcolormesh(T, R, Z, cmap='magma', shading='auto')
    fig.colorbar(pc, ax=ax, label='value', pad=0.1)
    ax.set_yticklabels([]); ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
