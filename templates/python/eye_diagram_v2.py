"""eye_diagram_v2: 眼图（升余弦脉冲 + 噪声 + ISI，多 trace 叠加）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def _rc_pulse(t, alpha):
    den = 1 - (2 * alpha * t) ** 2
    sing = np.isclose(np.abs(den), 0)
    h = np.sinc(t) * np.cos(np.pi * alpha * t) / np.where(sing, 1, den)
    return np.where(sing, np.pi / 4 * np.sinc(1 / (2 * alpha)), h)


def make_figure(alpha=0.35, sps=16, n_sym=600, noise=0.06, isi=0.25,
                title='Eye diagram (raised cosine, $\\alpha$=0.35)'):
    apply_theme()
    rng = np.random.default_rng(0)
    t = np.arange(-4 * sps, 4 * sps + 1) / sps
    h = _rc_pulse(t, alpha)
    sym = rng.choice([-1.0, 1.0], n_sym)
    x = np.zeros(n_sym * sps)
    x[::sps] = sym
    y = np.convolve(x, h, 'same')
    y[5:] += isi * y[:-5]                       # residual multipath ISI
    y += noise * rng.standard_normal(y.size)
    starts = np.arange(20, n_sym - 22) * sps
    idx = starts[:, None] + np.arange(2 * sps + 1)
    segs = y[idx]
    t_ui = (np.arange(2 * sps + 1) - sps) / sps
    fig, ax = plt.subplots()
    ax.plot(t_ui, segs.T, color=cycle(0), alpha=0.10, linewidth=0.7)
    ax.axvline(0, color=cycle(1), linestyle='--', linewidth=1, alpha=0.8)
    ax.text(0.03, ax.get_ylim()[1] * 0.92, 'optimum sampling', fontsize=7, color=cycle(1))
    ax.set_xlabel('time (UI)'); ax.set_ylabel('amplitude')
    ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
