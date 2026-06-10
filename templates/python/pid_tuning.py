"""pid_tuning: PID 不同参数的阶跃响应族."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
from theme import apply_theme
from palette import cycle

def make_figure(title='PID tuning step response'):
    apply_theme()
    fig, ax = plt.subplots()
    # plant: 1/(s^2 + s + 1)
    plant_num = [1.0]; plant_den = [1, 1, 1]
    cfgs = [(2, 0,   0,   'P  Kp=2'),
            (2, 1,   0,   'PI Kp=2 Ki=1'),
            (4, 2,   0.2, 'PID Kp=4 Ki=2 Kd=0.2'),
            (8, 4,   0.5, 'PID Kp=8 Ki=4 Kd=0.5')]
    t = np.linspace(0, 15, 1000)
    for i, (Kp, Ki, Kd, lab) in enumerate(cfgs):
        ctrl_num = [Kd, Kp, Ki]; ctrl_den = [1, 0]
        # closed loop = CP/(1+CP)
        open_num = np.convolve(ctrl_num, plant_num)
        open_den = np.convolve(ctrl_den, plant_den)
        cl_den = np.polyadd(open_den, np.concatenate([np.zeros(len(open_den)-len(open_num)), open_num]) if len(open_den) >= len(open_num) else open_num)
        sys = lti(open_num, cl_den)
        tt, y = step(sys, T=t)
        ax.plot(tt, y, color=cycle(i), label=lab)
    ax.axhline(1, color='gray', linestyle='--', linewidth=0.7)
    ax.set_xlabel('t'); ax.set_ylabel('y(t)'); ax.set_title(title)
    ax.legend(fontsize=7); ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
