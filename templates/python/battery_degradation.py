"""battery_degradation: 储能电池寿命衰减（容量保持率 vs 循环次数，DOD 分组 + EOL 线 + 实测散点）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _retention(n, dod):
    """容量衰减经验模型 (LiFePO4 风格):
    fade(%) = k * DOD^1.5 * sqrt(N)  — sqrt(N) 项对应 SEI 膜扩散控制生长,
    DOD^1.5 反映深放电加速机械/化学应力 (Wohler 类应力-寿命关系)。
    k 取 0.37 使 100% DOD 约 2900 次循环到 80% EOL。
    """
    k = 0.37
    return 100.0 - k * dod ** 1.5 * np.sqrt(n)

def make_figure(dods=None, title='Battery capacity fade vs cycle number'):
    apply_theme()
    rng = np.random.default_rng(0)
    if dods is None:
        dods = [0.6, 0.8, 1.0]
    eol = 80.0                                                # EOL 阈值 (%)
    n = np.linspace(0, 6000, 300)
    fig, ax = plt.subplots()
    for i, dod in enumerate(dods):
        q = _retention(n, dod)
        ax.plot(n, q, color=cycle(i), label=f'DOD = {dod*100:.0f}%')
        # 同模型加测量噪声的"实测"散点 (每 500 循环抽检一次)
        n_meas = np.arange(250, 6001, 500)
        q_meas = _retention(n_meas, dod) + rng.normal(0, 0.45, n_meas.size)
        ax.plot(n_meas, q_meas, linestyle='none', marker='o', markersize=4,
                markerfacecolor='white', markeredgecolor=cycle(i),
                markeredgewidth=1.0)
    ax.axhline(eol, color=cycle(7), linestyle='--', linewidth=1.2)
    ax.text(120, eol - 1.8, f'EOL = {eol:.0f}%', fontsize=8, color=cycle(7),
            va='top')
    ax.set_xlabel('cycle number'); ax.set_ylabel('capacity retention (%)')
    ax.set_title(title)
    ax.set_xlim(0, 6000); ax.set_ylim(62, 102)
    ax.legend(frameon=False, loc='lower left', title='model line / measured points')
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
