"""network_loss_map: 电网网损分布图（IEEE-14 风格拓扑：支路宽度=潮流，颜色=损耗）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from theme import apply_theme
from palette import cycle, sequential

# IEEE-14 节点示意坐标（仅作版图布置）与支路表 (i, j, r_pu)
NODES = {1: (0.0, 0.6), 2: (2.0, 0.0), 3: (5.0, 0.0), 4: (4.4, 1.5),
         5: (2.4, 1.5), 6: (2.0, 2.8), 7: (4.8, 2.3), 8: (6.0, 2.3),
         9: (4.4, 3.2), 10: (3.7, 3.9), 11: (2.8, 3.5), 12: (0.9, 3.6),
         13: (2.0, 4.3), 14: (3.5, 4.7)}
BRANCHES = [(1, 2, .01938), (1, 5, .05403), (2, 3, .04699), (2, 4, .05811),
            (2, 5, .05695), (3, 4, .06701), (4, 5, .01335), (4, 7, .00200),
            (4, 9, .00200), (5, 6, .00200), (6, 11, .09498), (6, 12, .12291),
            (6, 13, .06615), (7, 8, .00100), (7, 9, .00100), (9, 10, .03181),
            (9, 14, .12711), (10, 11, .08205), (12, 13, .22092), (13, 14, .17093)]
GEN_BUSES = {1, 2, 3, 6, 8}

def make_figure(flows=None, title='Network loss map (IEEE 14-bus style)'):
    """支路有功潮流 P (MW) 合成自典型 IEEE-14 潮流解;
    网损近似 P_loss ≈ r_pu * (P/Sbase)^2 * Sbase (V≈1 pu, 忽略无功分量),
    Sbase = 100 MVA。线宽 ∝ 潮流大小, 颜色 = 支路损耗, 变压器支路 r≈0 损耗小。
    """
    apply_theme()
    if flows is None:  # 典型潮流解的支路有功 (MW), 与 BRANCHES 一一对应
        flows = np.array([157, 75, 73, 56, 42, 23, 61, 28, 16, 44,
                          7, 8, 18, 21, 28, 5, 9, 4, 2, 6], dtype=float)
    sbase = 100.0
    r = np.array([b[2] for b in BRANCHES])
    loss = r * (flows / sbase) ** 2 * sbase                  # MW
    segs = [[NODES[i], NODES[j]] for i, j, _ in BRANCHES]
    lw = 0.8 + 4.0 * flows / flows.max()                     # 宽度 = 潮流
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    # 截掉色带最浅 20%, 避免低损耗支路在白底上不可见
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(sequential('orange')(np.linspace(0.2, 1.0, 256)))
    lc = LineCollection(segs, linewidths=lw, cmap=cmap, zorder=1)
    lc.set_array(loss)                                       # 颜色 = 损耗
    ax.add_collection(lc)
    fig.colorbar(lc, ax=ax, label='branch loss (MW)', pad=0.02)
    xy = np.array([NODES[k] for k in sorted(NODES)])
    is_gen = np.array([k in GEN_BUSES for k in sorted(NODES)])
    ax.scatter(xy[~is_gen, 0], xy[~is_gen, 1], s=130, facecolor='white',
               edgecolor=cycle(0), linewidth=1.4, zorder=3, label='Load bus')
    ax.scatter(xy[is_gen, 0], xy[is_gen, 1], s=130, facecolor=cycle(0),
               edgecolor=cycle(0), linewidth=1.4, zorder=3, label='Generator bus')
    for k, (x, y) in NODES.items():
        ax.annotate(str(k), (x, y), xytext=(0, 9), textcoords='offset points',
                    ha='center', fontsize=8, zorder=4)
    ax.text(0.02, 0.02, f'total loss = {loss.sum():.1f} MW',
            transform=ax.transAxes, fontsize=8)
    ax.set_xlim(-0.5, 6.6); ax.set_ylim(-0.5, 5.2)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title)
    ax.legend(frameon=False, loc='upper left', fontsize=7)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
