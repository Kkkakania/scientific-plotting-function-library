"""emi_spectrum: 传导 EMI 频谱（150 kHz~30 MHz 准峰值包络 vs CISPR 22 Class B 限值，超标段高亮）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def cispr22_classb_qp(f):
    """CISPR 22 Class B 传导发射准峰值限值 (dBuV):
    0.15-0.5 MHz: 66 → 56 dBuV 随 log(f) 线性下降; 0.5-5 MHz: 56; 5-30 MHz: 60。
    """
    f = np.asarray(f, dtype=float)
    lim = np.where(f < 0.5e6,
                   66.0 - 10.0 * np.log10(f / 0.15e6) / np.log10(0.5 / 0.15),
                   np.where(f < 5e6, 56.0, 60.0))
    return lim

def make_figure(f=None, qp=None, title='Conducted EMI spectrum vs CISPR 22 Class B'):
    """合成准峰值包络: 梯形开关波形频谱包络
    - 转折频率 f1 = 1/(pi*D*Tsw) 之前 0 dB/dec, f1~f2 间 -20 dB/dec,
      f2 = 1/(pi*tr) (tr 上升时间) 之后 -40 dB/dec;
    - 叠加 LISN/寄生谐振峰（~0.4 MHz 与 ~18 MHz 处 Q 峰）与测量纹波。
    """
    apply_theme()
    rng = np.random.default_rng(0)
    if f is None:
        f = np.logspace(np.log10(150e3), np.log10(30e6), 600)
        fsw, d, tr = 100e3, 0.4, 60e-9                       # 开关频率/占空比/上升时间
        f1, f2 = 1.0 / (np.pi * d / fsw), 1.0 / (np.pi * tr) # 包络两个转折点
        base = 92.0                                          # 低频平台 (dBuV)
        env = base - 20.0 * np.log10(np.maximum(f / f1, 1.0)) \
                   - 20.0 * np.log10(np.maximum(f / f2, 1.0))
        res1 = 9.0 / (1.0 + ((np.log10(f) - np.log10(0.4e6)) / 0.06) ** 2)
        res2 = 14.0 / (1.0 + ((np.log10(f) - np.log10(18e6)) / 0.05) ** 2)
        qp = env + res1 + res2 + rng.normal(0, 0.8, f.size)
    lim = cispr22_classb_qp(f)
    over = qp > lim
    fig, ax = plt.subplots()
    ax.semilogx(f / 1e6, qp, color=cycle(0), linewidth=1.0,
                label='Quasi-peak envelope')
    ax.semilogx(f / 1e6, lim, color=cycle(7), linestyle='--', linewidth=1.4,
                label='CISPR 22 Class B (QP)')
    qp_over = np.where(over, qp, np.nan)                     # 超标段红色高亮
    ax.semilogx(f / 1e6, qp_over, color='#C00000', linewidth=1.8,
                label='Above limit')
    ax.fill_between(f / 1e6, lim, qp, where=over, color='#C00000', alpha=0.20)
    ax.set_xlabel('frequency (MHz)'); ax.set_ylabel('amplitude (dBµV)')
    ax.set_title(title)
    ax.set_xlim(0.15, 30); ax.set_ylim(20, 100)
    ax.legend(frameon=False, loc='upper right')
    ax.grid(True, which='both', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
