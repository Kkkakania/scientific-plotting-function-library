"""diagram: 流程图/框图绘制助手（纯 matplotlib，无额外依赖）.

提供论文级流程图的积木：
- box / diamond / oval / parallelogram : 四种标准流程图节点
- arrow                               : 节点间带箭头连线（自动找边缘锚点）
- vflow                               : 垂直主干流程的自动布局

所有节点返回 (cx, cy, w, h)，方便继续连线。

用法::

    from diagram import box, diamond, arrow, new_canvas
    fig, ax = new_canvas(8, 10)
    a = box(ax, 4, 9, 'Start', kind='oval')
    b = box(ax, 4, 7, 'Initialize')
    arrow(ax, a, b)
"""
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch,
                                Ellipse, Polygon)

# 节点配色（与主题协调的低饱和方案）
STYLE = {
    'box':           dict(fc='#DCE9F5', ec='#2E5077'),
    'oval':          dict(fc='#DDEEDD', ec='#3A6B47'),
    'diamond':       dict(fc='#FBEED3', ec='#A8741A'),
    'parallelogram': dict(fc='#EBDDF0', ec='#6B3A78'),
    'process_alt':   dict(fc='#F5DCDC', ec='#8A3033'),
}


def new_canvas(w=8, h=10):
    """创建一张无坐标轴画布（数据坐标 = 排版坐标）."""
    fig, ax = plt.subplots(figsize=(w*0.8, h*0.8))
    ax.set_xlim(0, w); ax.set_ylim(0, h)
    ax.set_aspect('equal'); ax.axis('off')
    return fig, ax


def box(ax, cx, cy, text, w=2.4, h=0.9, kind='box', fontsize=9):
    """画一个流程图节点，返回 (cx, cy, w, h) 供 arrow 使用."""
    st = STYLE.get(kind, STYLE['box'])
    if kind == 'oval':
        ax.add_patch(Ellipse((cx, cy), w, h, facecolor=st['fc'],
                             edgecolor=st['ec'], lw=1.2, zorder=2))
    elif kind == 'diamond':
        pts = [(cx, cy + h*0.75), (cx + w*0.62, cy),
               (cx, cy - h*0.75), (cx - w*0.62, cy)]
        ax.add_patch(Polygon(pts, facecolor=st['fc'],
                             edgecolor=st['ec'], lw=1.2, zorder=2))
        h = h*1.5  # 锚点计算用实际高度
    elif kind == 'parallelogram':
        s = w*0.12
        pts = [(cx - w/2 + s, cy + h/2), (cx + w/2 + s, cy + h/2),
               (cx + w/2 - s, cy - h/2), (cx - w/2 - s, cy - h/2)]
        ax.add_patch(Polygon(pts, facecolor=st['fc'],
                             edgecolor=st['ec'], lw=1.2, zorder=2))
    else:
        ax.add_patch(FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                     boxstyle='round,pad=0.04,rounding_size=0.08',
                     facecolor=st['fc'], edgecolor=st['ec'], lw=1.2, zorder=2))
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize, zorder=3)
    return (cx, cy, w, h)


def _anchor(node, other):
    """从 node 边缘朝 other 方向取锚点（上下优先）."""
    cx, cy, w, h = node
    ox, oy = other[0], other[1]
    if abs(oy - cy) >= abs(ox - cx):          # 垂直为主
        return (cx, cy + h/2) if oy > cy else (cx, cy - h/2)
    return (cx + w/2, cy) if ox > cx else (cx - w/2, cy)


def arrow(ax, src, dst, label='', via=None, color='#404040', fontsize=8):
    """src → dst 箭头；via=[(x,y),...] 可走折线（每段独立画）."""
    pts = [_anchor(src, via[0] if via else dst)]
    if via:
        pts += list(via)
    pts.append(_anchor(dst, via[-1] if via else src))
    for i in range(len(pts) - 1):
        last = i == len(pts) - 2
        ax.add_patch(FancyArrowPatch(pts[i], pts[i+1],
                     arrowstyle='-|>' if last else '-',
                     mutation_scale=12, lw=1.1, color=color,
                     shrinkA=0, shrinkB=0, zorder=1))
    if label:
        mx = (pts[0][0] + pts[-1][0])/2
        my = (pts[0][1] + pts[-1][1])/2
        ax.text(mx + 0.12, my + 0.1, label, fontsize=fontsize,
                color=color, ha='left', zorder=3)


def vflow(ax, x, y_top, items, gap=1.4, w=2.6, h=0.9):
    """垂直主干流程：items=[(text, kind), ...]，自动连箭头，返回节点列表."""
    nodes = []
    for i, (text, kind) in enumerate(items):
        n = box(ax, x, y_top - i*gap, text, w=w, h=h, kind=kind)
        if nodes:
            arrow(ax, nodes[-1], n)
        nodes.append(n)
    return nodes
