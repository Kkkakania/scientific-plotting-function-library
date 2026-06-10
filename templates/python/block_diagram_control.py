"""block_diagram_control: 闭环控制系统框图（含求和点与反馈回路）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
from theme import apply_theme
from diagram import new_canvas, box, arrow

def make_figure(title='Closed-loop control block diagram'):
    apply_theme()
    fig, ax = new_canvas(12, 5)
    # 求和点
    sx, sy = 2.6, 3.2
    ax.add_patch(Circle((sx, sy), 0.22, fc='white', ec='#404040', lw=1.2, zorder=2))
    ax.text(sx - 0.32, sy + 0.28, '+', fontsize=10)
    ax.text(sx - 0.10, sy - 0.46, '−', fontsize=11)
    summ = (sx, sy, 0.44, 0.44)
    ctrl  = box(ax, 4.8, 3.2, 'PID\ncontroller', w=1.9, h=1.0)
    plant = box(ax, 7.6, 3.2, 'Plant\nG(s)', w=1.9, h=1.0)
    sens  = box(ax, 5.7, 1.3, 'Sensor\nH(s)', w=1.9, h=0.9, kind='process_alt')
    rin = (0.8, 3.2, 0.01, 0.01)
    ax.text(0.75, 3.45, 'r(t)', fontsize=9)
    arrow(ax, rin, summ); arrow(ax, summ, ctrl, label='e(t)')
    arrow(ax, ctrl, plant, label='u(t)')
    yout = (11.2, 3.2, 0.01, 0.01)
    arrow(ax, plant, yout, label='y(t)')
    # 反馈：从输出线分支 → sensor → 求和点下端
    ax.add_patch(Circle((10.2, 3.2), 0.05, color='#404040'))
    arrow(ax, (10.2, 3.2, 0.0, 0.0), sens, via=[(10.2, 1.3)])
    arrow(ax, sens, summ, via=[(sx, 1.3)])
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
