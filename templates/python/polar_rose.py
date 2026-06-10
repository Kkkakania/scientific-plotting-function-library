"""polar_rose: 极坐标玫瑰图（方向分布）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(n_sectors=16, title='Rose plot'):
    apply_theme(fig_size=(5.5, 5.5))
    rng = np.random.default_rng(0)
    theta = np.linspace(0, 2*np.pi, n_sectors, endpoint=False)
    radii = rng.uniform(0.3, 1.0, n_sectors)
    width = 2*np.pi / n_sectors
    cmap = sequential(hue='blue')
    colors = cmap(radii / radii.max())
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.bar(theta, radii, width=width, color=colors, edgecolor='w', linewidth=0.8)
    ax.set_title(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
