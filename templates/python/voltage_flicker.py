"""voltage_flicker: 电压闪变（调幅波形 + Pst 短时闪变值条形双面板）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(pst=None, title='Voltage flicker'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(3)
    # amplitude-modulated 50 Hz carrier; 8.8 Hz is the eye-brain most
    # sensitive flicker frequency (IEC 61000-4-15 weighting peak)
    f, fm, m = 50, 8.8, 0.08
    t = np.linspace(0, 1, 6000)
    env = 1 + m*np.sin(2*np.pi*fm*t)
    v = env*np.sin(2*np.pi*f*t)
    if pst is None:
        # 12 ten-minute short-term flicker severities; limit Pst = 1.0
        pst = np.clip(rng.normal(0.65, 0.18, 12), 0.2, None)
        pst[4], pst[5] = 1.25, 1.42      # arc-furnace heavy-melt intervals
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(t, v, color=cycle(0), linewidth=0.4)
    ax1.plot(t, env, color=cycle(1), linewidth=1.5, label='modulation envelope')
    ax1.plot(t, -env, color=cycle(1), linewidth=1.5)
    ax1.set_xlabel('time (s)'); ax1.set_ylabel('voltage (pu)')
    ax1.set_title(title); ax1.legend(loc='upper right')
    ax1.grid(True, linestyle=':', alpha=0.5)
    idx = np.arange(1, len(pst) + 1)
    colors = [cycle(1) if p > 1.0 else cycle(0) for p in pst]
    ax2.bar(idx, pst, color=colors, width=0.6)
    ax2.axhline(1.0, color=cycle(1), linestyle='--', linewidth=1.2,
                label='Pst limit = 1.0')
    ax2.set_xticks(idx)
    ax2.set_xlabel('10-min interval'); ax2.set_ylabel('Pst')
    ax2.set_title('Short-term flicker severity')
    ax2.legend(loc='upper left')
    ax2.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
