"""pv_mppt: MPPT 追踪过程（P-V 曲线 + 工作点轨迹）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='MPPT P-V tracking'):
    apply_theme()
    V = np.linspace(0, 22, 300)
    Isc = 8.2; Voc = 22
    I = np.clip(Isc * (1 - np.exp((V - Voc)/2)), 0, Isc); P = V * I
    fig, ax = plt.subplots()
    ax.plot(V, P, color=cycle(0))
    track_V = np.array([5, 8, 12, 15, 17, 18, 18.5])
    track_P = np.interp(track_V, V, P)
    ax.plot(track_V, track_P, '-o', color=cycle(1), markersize=7, label='tracking')
    Vmp = V[np.argmax(P)]
    ax.scatter(Vmp, P.max(), s=120, c='red', zorder=5, marker='*', label='MPP')
    ax.set_xlabel('V'); ax.set_ylabel('P (W)'); ax.set_title(title)
    ax.legend(); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
