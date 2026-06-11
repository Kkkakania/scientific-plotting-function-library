"""switching_loss_breakdown: 功率器件损耗分解（导通/开通/关断/反向恢复 × 开关频率堆叠柱）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(fsw_khz=None, title='Power device loss breakdown vs switching frequency'):
    """IGBT 半桥单管损耗模型（典型 600 V / 50 A 工况）:
    - 导通损耗  P_cond = Vce_sat * I_avg + r_ce * I_rms^2   (与 fsw 无关)
    - 开通损耗  P_on  = E_on  * fsw   (E_on  按数据手册开关能量, mJ/脉冲)
    - 关断损耗  P_off = E_off * fsw
    - 反向恢复  P_rr  = E_rr  * fsw   (续流二极管 Qrr 引起, 折算到开关管)
    开关三项随 fsw 线性增长, 导通项为常数 → 高频下开关损耗占主导。
    """
    apply_theme()
    if fsw_khz is None:
        fsw_khz = np.array([5.0, 10.0, 20.0, 50.0])
    fsw = np.asarray(fsw_khz, dtype=float) * 1e3            # Hz
    # 器件参数（典型 1200 V IGBT 模块 @ 600 V, 50 A, Tj=125 C）
    vce_sat, r_ce = 1.1, 9e-3                               # V, ohm
    i_avg, i_rms = 25.0, 35.0                               # A（半桥占空比 ~0.5）
    e_on, e_off, e_rr = 2.0e-3, 1.5e-3, 0.9e-3              # J/脉冲
    p_cond = np.full_like(fsw, vce_sat * i_avg + r_ce * i_rms**2)
    p_on, p_off, p_rr = e_on * fsw, e_off * fsw, e_rr * fsw
    parts = [p_cond, p_on, p_off, p_rr]
    labels = ['Conduction', 'Turn-on', 'Turn-off', 'Reverse recovery']
    fig, ax = plt.subplots()
    x = np.arange(len(fsw))
    bottom = np.zeros_like(fsw)
    for i, (p, lab) in enumerate(zip(parts, labels)):
        ax.bar(x, p, 0.55, bottom=bottom, color=cycle(i), label=lab)
        bottom += p
    for xi, tot in zip(x, bottom):                           # 顶部标总损耗
        ax.annotate(f'{tot:.0f} W', (xi, tot), xytext=(0, 3),
                    textcoords='offset points', ha='center', fontsize=8)
    ax.set_xticks(x); ax.set_xticklabels([f'{f:g}' for f in fsw_khz])
    ax.set_xlabel('switching frequency (kHz)')
    ax.set_ylabel('loss per device (W)')
    ax.set_title(title)
    ax.legend(frameon=False, loc='upper left')
    ax.grid(True, axis='y', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
