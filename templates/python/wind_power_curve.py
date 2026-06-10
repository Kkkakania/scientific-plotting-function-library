"""wind_power_curve: 风机功率曲线（理论曲线 + 实测散点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(v_in=3.0, v_rated=12.0, v_out=25.0, title='Wind turbine power curve'):
    apply_theme()
    rng = np.random.default_rng(0)
    v = np.linspace(0, 28, 400)
    P = np.where(v < v_in, 0,
        np.where(v < v_rated, (v**3 - v_in**3)/(v_rated**3 - v_in**3),
        np.where(v < v_out, 1.0, 0.0)))
    vs = rng.uniform(0.5, 27, 220)
    Ps = np.interp(vs, v, P) + rng.normal(0, 0.03, vs.size)
    Ps = np.clip(Ps + (vs > v_in)*rng.normal(0, 0.02, vs.size), 0, 1.08)
    fig, ax = plt.subplots()
    ax.scatter(vs, Ps, s=12, color=cycle(5), alpha=0.45, label='SCADA data')
    ax.plot(v, P, color=cycle(1), linewidth=2, label='design curve')
    for x, lab in [(v_in, 'cut-in'), (v_rated, 'rated'), (v_out, 'cut-out')]:
        ax.axvline(x, color='0.55', linestyle=':', linewidth=1)
        ax.text(x, 1.1, lab, ha='center', fontsize=8)
    ax.set_xlabel('wind speed (m/s)'); ax.set_ylabel('power (p.u.)'); ax.set_title(title)
    ax.set_ylim(-0.04, 1.18); ax.legend(loc='center right')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
