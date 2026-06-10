"""wind_rose: 风玫瑰图（风向 16 扇区 × 风速分级堆叠）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

def make_figure(title='Wind rose'):
    apply_theme()
    rng = np.random.default_rng(1)
    n_dir, bins = 16, ['0-3', '3-6', '6-9', '9-12', '>12 m/s']
    prevail = np.exp(-0.5*((np.arange(n_dir) - 4) % n_dir / 2.5)**2)             + 0.6*np.exp(-0.5*((np.arange(n_dir) - 12) % n_dir / 2.0)**2)
    freq = np.outer(prevail, [0.30, 0.30, 0.22, 0.12, 0.06])
    freq *= (1 + rng.uniform(-0.15, 0.15, freq.shape))
    freq = freq/freq.sum()*100
    theta = np.arange(n_dir)*2*np.pi/n_dir
    width = 2*np.pi/n_dir*0.9
    cmap = sequential('blue')
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(5.4, 5))
    bottom = np.zeros(n_dir)
    for j, b in enumerate(bins):
        ax.bar(theta, freq[:, j], width=width, bottom=bottom,
               color=cmap(0.25 + 0.75*j/(len(bins)-1)), edgecolor='w',
               linewidth=0.4, label=b)
        bottom += freq[:, j]
    ax.set_theta_zero_location('N'); ax.set_theta_direction(-1)
    ax.set_xticks(np.arange(0, 2*np.pi, np.pi/4))
    ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])
    ax.set_title(title, pad=18)
    ax.legend(loc='lower right', bbox_to_anchor=(1.25, -0.05), fontsize=7)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
