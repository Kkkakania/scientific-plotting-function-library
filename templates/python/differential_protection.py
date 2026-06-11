"""differential_protection: 差动保护比率制动特性（动作/制动区 + 故障样本散点）.

模型: 动作量 Id = |I1 + I2|, 制动量 Ir = |I1 - I2|/2 (或 max 形式).
两折线特性: Id_op = max(Id_min, k1*(Ir - Ir1) + Id_min, k2*(Ir - Ir2) + ...)
内部故障: Id 大、Ir 小 → 落在动作区; 外部故障/正常: Id 小 → 制动区.
"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _characteristic(ir, id_min=0.3, ir1=0.5, k1=0.5, ir2=3.0, k2=0.7):
    """两折线 + 起始水平段的比率制动特性."""
    seg1 = np.full_like(ir, id_min)
    seg2 = id_min + k1*(ir - ir1)
    seg3 = id_min + k1*(ir2 - ir1) + k2*(ir - ir2)
    return np.where(ir <= ir1, seg1, np.where(ir <= ir2, seg2, seg3))

def make_figure(title='Percentage differential protection characteristic'):
    apply_theme()
    rng = np.random.default_rng(8)
    ir = np.linspace(0, 6, 400)
    idop = _characteristic(ir)
    fig, ax = plt.subplots()
    # 动作区/制动区填充
    ax.fill_between(ir, idop, 6, color=cycle(1), alpha=0.15)
    ax.fill_between(ir, 0, idop, color=cycle(0), alpha=0.12)
    ax.plot(ir, idop, color='0.25', linewidth=1.8, label='operating characteristic')
    ax.text(1.0, 4.6, 'OPERATE', fontsize=10, color=cycle(1), fontweight='bold')
    ax.text(4.0, 0.8, 'RESTRAIN', fontsize=10, color=cycle(0), fontweight='bold')
    # 内部故障样本: 穿越电流小、差流大（沿 Id ≈ 2*Ir 即 I2 反向）
    ir_int = rng.uniform(0.3, 2.6, 28)
    id_int = ir_int*2*rng.uniform(0.85, 1.0, 28) + rng.normal(0, 0.08, 28)
    # 外部故障/正常负荷: 差流仅由 CT 误差产生 (~5~15% Ir)
    ir_ext = rng.uniform(0.3, 5.6, 34)
    id_ext = ir_ext*rng.uniform(0.03, 0.16, 34) + np.abs(rng.normal(0, 0.04, 34))
    ax.scatter(ir_int, id_int, s=26, color=cycle(1), marker='^',
               edgecolor='white', linewidth=0.5, label='internal faults', zorder=3)
    ax.scatter(ir_ext, id_ext, s=24, color=cycle(0), marker='o',
               edgecolor='white', linewidth=0.5, label='external faults / load', zorder=3)
    # 拐点标注
    for x_, lab in [(0.5, 'knee 1'), (3.0, 'knee 2')]:
        y_ = _characteristic(np.array([x_]))[0]
        ax.plot(x_, y_, 's', color='0.25', ms=4)
        ax.annotate(lab, (x_, y_), xytext=(6, -12), textcoords='offset points', fontsize=7)
    ax.set_xlabel('restraint current $I_r$ (p.u.)')
    ax.set_ylabel('differential current $I_d$ (p.u.)')
    ax.set_title(title); ax.set_xlim(0, 6); ax.set_ylim(0, 6)
    ax.legend(loc='upper left', fontsize=8)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
