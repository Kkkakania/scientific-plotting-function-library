"""sankey_multistage: 三级桑基（源→中间→汇，曲线流带）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from theme import apply_theme
from palette import cycle


def _band(ax, x0, x1, yb0, yt0, yb1, yt1, color, alpha=0.45):
    t = np.linspace(0, 1, 60)
    s = (1 - np.cos(np.pi * t)) / 2
    x = x0 + (x1 - x0) * t
    ax.fill_between(x, yb0 + (yb1 - yb0) * s, yt0 + (yt1 - yt0) * s,
                    color=color, alpha=alpha, lw=0)


def _stack(vals, gap):
    top = sum(vals) + gap * (len(vals) - 1)
    ys = []
    y = top
    for v in vals:
        ys.append((y - v, y)); y -= v + gap
    return ys


def make_figure(title='Three-stage Sankey flow'):
    apply_theme()
    L1 = np.array([[20., 10.], [10., 15.], [5., 10.]])   # sources -> mid
    L2 = np.array([[15., 12., 8.], [10., 10., 15.]])     # mid -> sinks
    src, mid, snk = L1.sum(1), L1.sum(0), L2.sum(1)
    sink_v = L2.sum(0)
    gap = 4.0; w = 0.16
    xs = [0.0, 1.6, 3.2]
    ys_s, ys_m, ys_t = _stack(src, gap), _stack(mid, gap), _stack(sink_v, gap)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    off_o = [ys_s[i][1] for i in range(3)]
    off_i = [ys_m[j][1] for j in range(2)]
    for i in range(3):
        for j in range(2):
            v = L1[i, j]
            if v > 0:
                _band(ax, xs[0] + w, xs[1], off_o[i] - v, off_o[i],
                      off_i[j] - v, off_i[j], cycle(i))
                off_o[i] -= v; off_i[j] -= v
    off_o = [ys_m[i][1] for i in range(2)]
    off_i = [ys_t[j][1] for j in range(3)]
    for i in range(2):
        for j in range(3):
            v = L2[i, j]
            if v > 0:
                _band(ax, xs[1] + w, xs[2], off_o[i] - v, off_o[i],
                      off_i[j] - v, off_i[j], cycle(3 + i))
                off_o[i] -= v; off_i[j] -= v
    names = [['S1', 'S2', 'S3'], ['M1', 'M2'], ['T1', 'T2', 'T3']]
    cols = [[cycle(i) for i in range(3)], [cycle(3 + i) for i in range(2)],
            ['#7A828A'] * 3]
    for x, ys, nm, cc in zip(xs, [ys_s, ys_m, ys_t], names, cols):
        for (y0, y1), label, c in zip(ys, nm, cc):
            ax.add_patch(Rectangle((x, y0), w, y1 - y0, color=c, zorder=3))
            ax.text(x + w / 2, (y0 + y1) / 2, label, ha='center',
                    va='center', fontsize=8, color='white', zorder=4)
    ax.set_xlim(-0.25, 3.6); ax.axis('off')
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
