"""zoomed_inset: 主图 + 局部放大插图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from theme import apply_theme
from palette import cycle

def make_figure(t=None, y=None, zoom_xlim=(0.40, 0.46), title='Zoomed inset'):
    apply_theme(fig_size=(7, 4))
    if t is None:
        t = np.linspace(0, 1, 2000)
        y = np.sin(2*np.pi*5*t) + 0.3*np.sin(2*np.pi*50*t)
    fig, ax = plt.subplots()
    ax.plot(t, y, color=cycle(0), linewidth=1)
    ax.set_xlabel('t'); ax.set_ylabel('y'); ax.set_title(title)
    axins = inset_axes(ax, width='35%', height='35%', loc='upper right')
    axins.plot(t, y, color=cycle(0), linewidth=1)
    axins.set_xlim(*zoom_xlim); axins.set_ylim(-1.5, 1.5)
    axins.set_xticks([]); axins.set_yticks([])
    mark_inset(ax, axins, loc1=2, loc2=4, fc='none', ec='gray', lw=0.8)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
