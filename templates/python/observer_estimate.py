"""observer_estimate: 状态观测器估计 vs 真实状态 + 误差衰减."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Observer estimate'):
    apply_theme(fig_size=(8, 5))
    t = np.linspace(0, 5, 500)
    true = np.sin(2*t)*np.exp(-0.3*t)
    err  = 0.8*np.exp(-1.5*t)
    est  = true + err*np.cos(5*t)
    fig, (a1, a2) = plt.subplots(2, 1, sharex=True)
    a1.plot(t, true, color=cycle(0), label='true x')
    a1.plot(t, est,  '--', color=cycle(1), label='estimate x̂')
    a1.set_ylabel('state'); a1.set_title(title)
    a1.legend(); a1.grid(True, linestyle=':', alpha=0.5)
    a2.plot(t, true - est, color=cycle(2))
    a2.axhline(0, color='gray', linewidth=0.5)
    a2.set_xlabel('t'); a2.set_ylabel('error x - x̂')
    a2.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
