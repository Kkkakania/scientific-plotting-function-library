"""bar_overlay_mckinsey: 麦肯锡商务风叠加柱状图（同基线宽窄两层对比）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle


def make_figure(ref=None, main=None, labels=None,
                ref_name='All other respondents',
                main_name='Top performers',
                title='Capabilities organizations invested in'):
    apply_theme()
    if ref is None:
        ref = np.array([72, 65, 58, 47, 39])     # 宽柱：对照组（底层）
        main = np.array([88, 71, 75, 52, 33])    # 窄柱：重点组（顶层）
        labels = ['Data architecture', 'Cloud platforms', 'Advanced analytics',
                  'Process automation', 'Digital talent']
    ref = np.asarray(ref, dtype=float); main = np.asarray(main, dtype=float)
    y = np.arange(len(ref))
    c_ref, c_main = '0.82', cycle(0)
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    # 同一基线两层 barh：宽灰底 + 窄彩色，形成"叠加"对比而非堆叠
    ax.barh(y, ref, height=0.72, color=c_ref, edgecolor='none', zorder=1,
            label=ref_name)
    ax.barh(y, main, height=0.34, color=c_main, edgecolor='none', zorder=2,
            label=main_name)
    # 数值长在柱端内侧
    for yi, (r, m) in enumerate(zip(ref, main)):
        ax.text(r - 1.5, yi - 0.26, '%.0f' % r, ha='right', va='center',
                fontsize=9, color='0.35')
        ax.text(m - 1.5, yi, '%.0f' % m, ha='right', va='center',
                fontsize=9, color='white', fontweight='bold')
    # 类目标签代替 y 轴
    for yi, lab in zip(y, labels):
        ax.text(-2.5, yi, lab, ha='right', va='center', fontsize=9)
    ax.set_title(title, loc='left', fontweight='bold', pad=24)
    ax.text(0, len(y) - 0.35, 'share of respondents (%)', fontsize=8,
            color='0.45', va='top')
    ax.invert_yaxis()
    ax.set_xlim(-38, 100)
    ax.axis('off')
    ax.legend(frameon=False, loc='lower left',
              bbox_to_anchor=(0.0, 1.0), ncol=2, handlelength=0.9,
              handleheight=0.9, fontsize=9)
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
