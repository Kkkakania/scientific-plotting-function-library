"""power_triangle: 有功-无功-视在功率三角形."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(P=8, Q=6, title='Power triangle'):
    apply_theme(fig_size=(6, 5))
    S = np.hypot(P, Q); phi = np.arctan2(Q, P)
    fig, ax = plt.subplots()
    ax.annotate('', xy=(P, 0),   xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=cycle(0), lw=2))
    ax.annotate('', xy=(P, Q),   xytext=(P, 0), arrowprops=dict(arrowstyle='->', color=cycle(1), lw=2))
    ax.annotate('', xy=(P, Q),   xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=cycle(2), lw=2))
    ax.text(P/2, -0.4, f'P = {P} kW',   color=cycle(0), ha='center')
    ax.text(P+0.3, Q/2, f'Q = {Q} kVAr', color=cycle(1))
    ax.text(P/2-0.3, Q/2+0.4, f'S = {S:.2f} kVA', color=cycle(2))
    arc = plt.matplotlib.patches.Arc((0,0), 2, 2, angle=0, theta1=0, theta2=np.degrees(phi), color='k')
    ax.add_patch(arc)
    ax.text(1.5*np.cos(phi/2), 1.5*np.sin(phi/2), f'φ = {np.degrees(phi):.1f}°', fontsize=9)
    ax.set_xlim(-1, P+3); ax.set_ylim(-1.5, Q+2)
    ax.set_aspect('equal'); ax.set_xlabel('P'); ax.set_ylabel('Q'); ax.set_title(title)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
