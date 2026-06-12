"""hive_plot: 蜂巢图（3 轴按节点类别放置，轴间贝塞尔连线）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(n_per=6, title='Hive plot (three node classes)'):
    apply_theme()
    rng = np.random.default_rng(11)
    ax_ang = np.deg2rad([90, 210, 330])
    r0, r1 = 0.55, 3.0
    radii = np.linspace(0.95, 2.85, n_per)
    pos = {(a, k): (radii[k] * np.cos(ax_ang[a]), radii[k] * np.sin(ax_ang[a]))
           for a in range(3) for k in range(n_per)}
    fig, ax = plt.subplots(figsize=(5.6, 5.4))
    ax.set_xlim(-3.7, 3.7); ax.set_ylim(-3.2, 3.9)
    ax.set_aspect('equal'); ax.axis('off')
    t = np.linspace(0, 1, 50)[:, None]
    pairs = [(0, 1), (1, 2), (2, 0)]
    for pi, (a, b) in enumerate(pairs):       # bezier links between axes
        for _ in range(8):
            ka, kb = rng.integers(0, n_per, 2)
            p0 = np.array(pos[(a, ka)]); p1 = np.array(pos[(b, kb)])
            mid_ang = np.angle(np.exp(1j * ax_ang[a]) + np.exp(1j * ax_ang[b]))
            rm = 0.55 * (radii[ka] + radii[kb]) / 2
            pc = rm * np.array([np.cos(mid_ang), np.sin(mid_ang)])
            bez = (1 - t)**2 * p0 + 2 * t * (1 - t) * pc + t**2 * p1
            ax.plot(bez[:, 0], bez[:, 1], color=cycle(pi), lw=1.1,
                    alpha=0.5, zorder=1)
    for a in range(3):                        # axes + nodes
        ax.plot([r0 * np.cos(ax_ang[a]), r1 * np.cos(ax_ang[a])],
                [r0 * np.sin(ax_ang[a]), r1 * np.sin(ax_ang[a])],
                color='#7A828A', lw=2.5, zorder=2,
                solid_capstyle='round')
        xs = [pos[(a, k)][0] for k in range(n_per)]
        ys = [pos[(a, k)][1] for k in range(n_per)]
        ax.scatter(xs, ys, s=55, color=cycle(a), zorder=3,
                   edgecolors='white', linewidths=0.7)
        lx, ly = 3.45 * np.cos(ax_ang[a]), 3.45 * np.sin(ax_ang[a])
        ax.text(lx, ly, f'Type {chr(65 + a)}', ha='center', va='center',
                fontsize=9)
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
