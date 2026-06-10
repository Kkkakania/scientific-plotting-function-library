"""motor_torque_speed: 感应电机转矩-转速特性族（变频调速）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential, cycle

def make_figure(title='Induction motor torque-speed (V/f control)'):
    apply_theme()
    cmap = sequential('blue')
    fig, ax = plt.subplots()
    R2, X = 0.08, 0.45
    freqs = [10, 20, 30, 40, 50]
    for i, f in enumerate(freqs):
        ws = f/50
        w = np.linspace(0, ws, 300)
        s = np.clip((ws - w)/np.maximum(ws, 1e-6), 1e-4, 1)
        T = 2.2*ws**0 * (R2/s) / ((R2/s)**2 + (X*f/50)**2) * (f/50)**0
        T = T/ T.max() * (2.0 if f == 50 else 2.0)
        ax.plot(w*1500, T, color=cmap(0.3 + 0.7*i/(len(freqs)-1)), label=f'{f} Hz')
    ax.plot([0, 1500], [1.0, 1.0], color=cycle(1), linestyle='--', lw=1, label='load torque')
    ax.set_xlabel('speed (rpm)'); ax.set_ylabel('torque (p.u.)'); ax.set_title(title)
    ax.legend(fontsize=7); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
