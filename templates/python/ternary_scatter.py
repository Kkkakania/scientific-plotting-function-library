"""ternary_scatter: 三元相图散点（重心坐标投影，纯 matplotlib 零依赖）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import sequential

SQRT3_2 = np.sqrt(3) / 2


def _tern2xy(a, b, c):
    """重心坐标 (a,b,c)（a+b+c=1）→ 平面坐标。顶点 A=(0,0) B=(1,0) C=(0.5,√3/2)."""
    s = a + b + c
    return (b + 0.5 * c) / s, SQRT3_2 * c / s


def make_figure(abc=None, values=None, labels=('Cu', 'Zn', 'Ni'),
                title='Ternary composition diagram'):
    apply_theme(fig_size=(5.6, 4.8))
    if abc is None:
        rng = np.random.default_rng(0)
        abc = rng.dirichlet([2.5, 1.8, 1.2], 120)         # 合成合金成分
        values = 200 + 300*abc[:, 0] - 120*abc[:, 2] + rng.normal(0, 12, 120)
    a, b, c = abc[:, 0], abc[:, 1], abc[:, 2]
    fig, ax = plt.subplots()
    # 三角形边框
    tri_x, tri_y = _tern2xy(np.array([1, 0, 0, 1]), np.array([0, 1, 0, 0]),
                            np.array([0, 0, 1, 0]))
    ax.plot(tri_x, tri_y, color='0.25', lw=1.0, zorder=3)
    # 网格线：三族等值线（每 20%），矢量化生成
    for f in np.arange(0.2, 1.0, 0.2):
        g = 1 - f
        for p0, p1 in [((f, g, 0), (f, 0, g)),            # a = f
                       ((g, f, 0), (0, f, g)),            # b = f
                       ((g, 0, f), (0, g, f))]:           # c = f
            x0, y0 = _tern2xy(*map(np.asarray, zip(p0, p1)))
            ax.plot(x0, y0, linestyle=':', color='0.75', lw=0.6, zorder=1)
        # 轴刻度标注（沿三条边）
        ax.text(*_tern2xy(f, 1-f, 0), f'{f:.1f}', fontsize=6.5,
                ha='center', va='top', color='0.4')
    # 数据点
    x, y = _tern2xy(a, b, c)
    sc = ax.scatter(x, y, c=values, cmap=sequential('blue'), s=22,
                    edgecolors='0.3', linewidths=0.3, zorder=4)
    cb = fig.colorbar(sc, ax=ax, shrink=0.8, pad=0.02)
    cb.set_label('hardness (HV)')
    # 顶点标签
    ax.text(-0.04, -0.03, labels[0], ha='right', va='top', fontsize=10)
    ax.text(1.04, -0.03, labels[1], ha='left', va='top', fontsize=10)
    ax.text(0.5, SQRT3_2 + 0.04, labels[2], ha='center', va='bottom', fontsize=10)
    ax.set_xlim(-0.12, 1.12); ax.set_ylim(-0.12, SQRT3_2 + 0.12)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(title)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
