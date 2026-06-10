"""ramp_response: 一阶/二阶系统对单位斜坡的响应."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Ramp response'):
    apply_theme()
    t = np.linspace(0, 8, 500)
    ramp = t
    # 一阶
    tau = 1.0
    y1 = t - tau + tau*np.exp(-t/tau)
    # 二阶 (zeta=0.5, wn=2)
    z, wn = 0.5, 2.0; wd = wn*np.sqrt(1-z**2)
    y2 = t - 2*z/wn + np.exp(-z*wn*t)*(2*z/wn*np.cos(wd*t) - (1-2*z**2)/wd*np.sin(wd*t))
    fig, ax = plt.subplots()
    ax.plot(t, ramp, '--', color='gray', label='input r(t) = t')
    ax.plot(t, y1, color=cycle(0), label='1st-order, τ=1')
    ax.plot(t, y2, color=cycle(1), label='2nd-order, ζ=0.5')
    ax.set_xlabel('t'); ax.set_ylabel('y(t)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
