"""treemap_basic: 矩形树状图（自实现 squarified 布局，零第三方依赖）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from theme import apply_theme
from palette import cycle


def _layout_row(areas, x, y, w, h):
    """把一行/一列矩形铺进 (x,y,w,h) 的短边方向，返回矩形列表和剩余区域."""
    total = sum(areas)
    rects = []
    if w >= h:                       # 竖排成一列，列宽 = total/h
        col_w = total / h
        cy = y
        for a in areas:
            rects.append((x, cy, col_w, a / col_w))
            cy += a / col_w
        return rects, (x + col_w, y, w - col_w, h)
    row_h = total / w                # 横排成一行
    cx = x
    for a in areas:
        rects.append((cx, y, a / row_h, row_h))
        cx += a / row_h
    return rects, (x, y + row_h, w, h - row_h)


def _worst_ratio(areas, side):
    """该行铺在长度 side 的短边上时的最差纵横比."""
    total = sum(areas)
    thick = total / side
    ratios = [max(thick / (a / thick), (a / thick) / thick) for a in areas]
    return max(ratios)


def squarify(sizes, x=0.0, y=0.0, w=100.0, h=100.0):
    """squarified treemap：sizes 降序排列，返回与 sizes 同序的 (x,y,w,h) 列表."""
    sizes = np.asarray(sizes, dtype=float)
    areas = list(sizes * (w * h) / sizes.sum())
    rects = []
    row = []
    while areas:
        side = min(w, h)
        cand = row + [areas[0]]
        if not row or _worst_ratio(cand, side) <= _worst_ratio(row, side):
            row = cand
            areas.pop(0)
        else:                        # 纵横比开始变差 → 固化当前行
            placed, (x, y, w, h) = _layout_row(row, x, y, w, h)
            rects.extend(placed)
            row = []
    if row:
        placed, _ = _layout_row(row, x, y, w, h)
        rects.extend(placed)
    return rects


def make_figure(sizes=None, labels=None, title='Research budget treemap'):
    apply_theme(fig_size=(6, 4.2))
    if sizes is None:
        rng = np.random.default_rng(0)
        labels = ['Materials', 'Equipment', 'Personnel', 'Computing',
                  'Travel', 'Publication', 'Outreach', 'Misc']
        sizes = np.sort(rng.gamma(3.0, 12.0, len(labels)))[::-1]
    order = np.argsort(sizes)[::-1]              # 算法要求降序
    sizes_d = np.asarray(sizes, dtype=float)[order]
    labels_d = [labels[i] for i in order]
    rects = squarify(sizes_d)
    fig, ax = plt.subplots()
    total = sizes_d.sum()
    for i, ((rx, ry, rw, rh), lab) in enumerate(zip(rects, labels_d)):
        ax.add_patch(Rectangle((rx, ry), rw, rh, facecolor=cycle(i),
                               edgecolor='white', linewidth=1.5, alpha=0.9))
        if rw * rh > 250:                        # 太小的块不放文字
            ax.text(rx + rw/2, ry + rh/2, f'{lab}\n{100*sizes_d[i]/total:.1f}%',
                    ha='center', va='center', fontsize=7, color='white')
    ax.set_xlim(0, 100); ax.set_ylim(0, 100)
    ax.set_aspect('equal'); ax.invert_yaxis()
    ax.set_title(title); ax.axis('off')
    fig.tight_layout()
    return fig


if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
