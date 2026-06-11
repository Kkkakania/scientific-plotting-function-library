"""thermal_transient: 器件结温暂态（Foster 3 阶 RC 热网络阶跃响应，多功率等级）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(p_levels=None, title='Junction temperature step response (Foster network)'):
    """Foster 热网络阶跃功率响应:
    Zth(t) = sum_i R_i * (1 - exp(-t / tau_i)),  tau_i = R_i * C_i
    Tj(t)  = Ta + P * Zth(t)
    取典型 IGBT 模块结-环境 3 阶参数（含散热器）:
    R = [0.05, 0.18, 0.32] K/W（芯片/基板/散热器层），tau = [2 ms, 80 ms, 2 s]。
    稳态 Zth = sum(R) = 0.55 K/W → 200 W 时温升 110 K。
    """
    apply_theme()
    if p_levels is None:
        p_levels = [100.0, 200.0, 300.0]                    # W 阶跃功率
    ta, tj_max = 40.0, 150.0                                # 环境温度 / 最大结温 (C)
    r = np.array([0.05, 0.18, 0.32])                        # K/W
    tau = np.array([2e-3, 8e-2, 2.0])                       # s
    t = np.logspace(-4, 1.3, 400)                           # 0.1 ms ~ 20 s
    zth = np.sum(r * (1.0 - np.exp(-t[:, None] / tau)), axis=1)
    fig, ax = plt.subplots()
    for i, p in enumerate(p_levels):
        ax.semilogx(t, ta + p * zth, color=cycle(i), label=f'P = {p:g} W')
    ax.axhline(tj_max, color=cycle(1), linestyle='--', linewidth=1.2)
    ax.text(t[0] * 1.5, tj_max + 2, f'Tj,max = {tj_max:g} °C',
            fontsize=8, color=cycle(1))
    ax.set_xlabel('time (s)'); ax.set_ylabel('junction temperature (°C)')
    ax.set_title(title)
    ax.set_xlim(t[0], t[-1]); ax.set_ylim(ta - 5, ta + max(p_levels) * zth[-1] + 25)
    ax.legend(frameon=False, loc='upper left')
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
