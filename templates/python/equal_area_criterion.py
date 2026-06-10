"""equal_area_criterion: 等面积法则（暂态稳定判据）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(Pm=0.8, title='Equal-area criterion'):
    apply_theme()
    d = np.linspace(0, np.pi, 400)
    Pe_pre, Pe_fault, Pe_post = 1.8*np.sin(d), 0.4*np.sin(d), 1.3*np.sin(d)
    d0 = np.arcsin(Pm/1.8); dc = 1.05; dmax = np.pi - np.arcsin(Pm/1.3)
    fig, ax = plt.subplots()
    ax.plot(np.degrees(d), Pe_pre, color=cycle(0), label='pre-fault')
    ax.plot(np.degrees(d), Pe_fault, color=cycle(1), label='during fault')
    ax.plot(np.degrees(d), Pe_post, color=cycle(2), label='post-fault')
    ax.axhline(Pm, color='0.3', linewidth=1, linestyle='--')
    m1 = (d >= d0) & (d <= dc)
    ax.fill_between(np.degrees(d[m1]), Pe_fault[m1], Pm, color=cycle(1), alpha=0.3)
    m2 = (d >= dc) & (d <= dmax) & (1.3*np.sin(d) >= Pm)
    ax.fill_between(np.degrees(d[m2]), Pm, Pe_post[m2], color=cycle(2), alpha=0.3)
    ax.text(np.degrees((d0+dc)/2), Pm-0.12, 'A1', ha='center', fontsize=9)
    ax.text(np.degrees((dc+dmax)/2), Pm+0.14, 'A2', ha='center', fontsize=9)
    ax.set_xlabel('rotor angle δ (deg)'); ax.set_ylabel('power (p.u.)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5); ax.set_ylim(0, 2)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
