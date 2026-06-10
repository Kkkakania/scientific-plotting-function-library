"""three_phase_waveform: 三相正弦电压时域 + 相量图."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(f=50, Um=311, title='Three-phase'):
    apply_theme(fig_size=(10, 4.5))
    t = np.linspace(0, 0.04, 1000)
    ua = Um*np.sin(2*np.pi*f*t)
    ub = Um*np.sin(2*np.pi*f*t - 2*np.pi/3)
    uc = Um*np.sin(2*np.pi*f*t + 2*np.pi/3)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    for i, (u, lab) in enumerate(zip([ua, ub, uc], ['Ua', 'Ub', 'Uc'])):
        ax1.plot(t*1000, u, color=cycle(i), label=lab)
    ax1.axhline(0, color='gray', linewidth=0.5)
    ax1.set_xlabel('t (ms)'); ax1.set_ylabel('voltage (V)')
    ax1.set_title('Time domain'); ax1.legend(); ax1.grid(True, linestyle=':', alpha=0.5)
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    for i, (ang, lab) in enumerate(zip([0, -2*np.pi/3, 2*np.pi/3], ['Ua', 'Ub', 'Uc'])):
        ax2.annotate('', xy=(ang, Um), xytext=(0, 0),
                     arrowprops=dict(arrowstyle='->', color=cycle(i), lw=2))
        ax2.text(ang, Um*1.1, lab, ha='center', color=cycle(i))
    ax2.set_rticks([100, 200, 300]); ax2.set_title('Phasor', pad=15)
    fig.suptitle(title); fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
