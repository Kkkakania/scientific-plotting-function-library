"""pq_injection_heatmap: 电网节点 P/Q 注入热力图（IEEE-14 节点 × 24 小时，发散色图）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import diverging

def _demo_injections():
    rng = np.random.default_rng(42)
    hours = np.arange(24)
    profile = 0.7 + 0.3*np.sin((hours - 6)/24*2*np.pi)   # daily load shape
    gen_buses = [0, 1, 2, 5, 7]                           # IEEE-14: 1,2,3,6,8
    p_base = rng.uniform(-0.6, -0.15, 14)                 # loads draw P (<0)
    p_base[gen_buses] = [2.3, 0.4, 0.0, 0.0, 0.0]
    p_base[gen_buses] += rng.uniform(0.2, 0.9, 5)         # generators inject (>0)
    q_base = 0.35*p_base + rng.normal(0, 0.05, 14)
    P = p_base[:, None]*profile[None, :] + rng.normal(0, 0.03, (14, 24))
    Q = q_base[:, None]*profile[None, :] + rng.normal(0, 0.02, (14, 24))
    return P, Q

def make_figure(P=None, Q=None, title='Bus P/Q injection profile (IEEE-14)'):
    apply_theme(fig_size=(8.5, 4.2))
    if P is None:
        P, Q = _demo_injections()
    fig, axes = plt.subplots(1, 2, sharey=True)
    cmap = diverging()
    for ax, M, name in zip(axes, [P, Q], ['Active power P (p.u.)',
                                          'Reactive power Q (p.u.)']):
        vmax = np.abs(M).max()
        im = ax.pcolormesh(np.arange(25), np.arange(15), M, cmap=cmap,
                           vmin=-vmax, vmax=vmax, shading='flat')
        ax.set_xlabel('hour of day'); ax.set_title(name)
        ax.set_xticks(np.arange(0, 25, 6))
        ax.set_yticks(np.arange(14) + 0.5)
        ax.set_yticklabels([f'{b}' for b in range(1, 15)], fontsize=7)
        fig.colorbar(im, ax=ax, label='injection (p.u.)', shrink=0.9)
    axes[0].set_ylabel('bus number')
    fig.suptitle(title)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
