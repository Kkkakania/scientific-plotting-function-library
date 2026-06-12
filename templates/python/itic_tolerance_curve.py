"""itic_tolerance_curve: ITIC/CBEMA 电压耐受曲线（半对数包络 + 事件散点分区着色）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

# ITIC (2000) envelope vertices: duration (s) vs voltage (% of nominal).
# Steps are encoded by nearly-coincident x pairs so interp stays monotonic.
UP_D = np.array([1e-3, 3e-3, 3.0003e-3, 0.5, 0.50005, 10.0])
UP_V = np.array([200., 200., 140., 140., 120., 120.])
LO_D = np.array([1e-3, 0.02, 0.020002, 0.5, 0.50005, 10.0])
LO_V = np.array([0., 0., 70., 70., 80., 80.])


def _env(d, dd, vv):
    """Envelope value at duration d (piecewise linear in log-duration)."""
    return np.interp(np.log10(d), np.log10(dd), vv)


def make_figure(events=None, title='ITIC voltage tolerance curve'):
    apply_theme()
    if events is None:
        # synthetic monitored events: mostly sags, a few swells/impulses
        rng = np.random.default_rng(7)
        n = 60
        dur = 10**rng.uniform(-3, 1, n)
        mag = np.concatenate([rng.uniform(10, 110, n - 15),
                              rng.uniform(112, 230, 15)])
        rng.shuffle(mag)
        events = np.column_stack([dur, mag])
    d = np.logspace(-3, 1, 500)
    up, lo = _env(d, UP_D, UP_V), _env(d, LO_D, LO_V)
    fig, ax = plt.subplots()
    # region shading: above upper = prohibited, between = ride-through, below = no-damage
    ax.fill_between(d, up, 240, color=cycle(1), alpha=0.10)
    ax.fill_between(d, lo, up, color=cycle(2), alpha=0.10)
    ax.fill_between(d, 0, lo, color=cycle(7), alpha=0.18)
    ax.plot(d, up, color=cycle(1), linewidth=1.5, label='upper limit')
    ax.plot(d, lo, color=cycle(7), linewidth=1.5, label='lower limit')
    ed, em = events[:, 0], events[:, 1]
    hi = em > _env(ed, UP_D, UP_V)
    lo_ev = em < _env(ed, LO_D, LO_V)
    ok = ~hi & ~lo_ev
    ax.scatter(ed[ok], em[ok], s=16, color=cycle(2), zorder=3, label='ride-through')
    ax.scatter(ed[hi], em[hi], s=18, color=cycle(1), marker='^', zorder=3, label='prohibited')
    ax.scatter(ed[lo_ev], em[lo_ev], s=18, color=cycle(7), marker='v', zorder=3, label='no-damage trip')
    ax.axhline(100, color='0.6', linewidth=0.6, linestyle='--')
    ax.set_xscale('log'); ax.set_ylim(0, 240); ax.set_xlim(1e-3, 10)
    ax.set_xlabel('event duration (s)'); ax.set_ylabel('voltage (% of nominal)')
    ax.set_title(title)
    ax.legend(loc='upper right', fontsize=7)
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
