"""flowchart_algorithm: 算法流程图（含判断分支与循环回边）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from diagram import new_canvas, box, arrow

def make_figure(title='Algorithm flowchart'):
    apply_theme()
    fig, ax = new_canvas(9, 11)
    start = box(ax, 4.5, 10.2, 'Start', kind='oval', w=2.0)
    init  = box(ax, 4.5, 8.8, 'Initialize population\nk = 0')
    evalb = box(ax, 4.5, 7.4, 'Evaluate fitness')
    conv  = box(ax, 4.5, 5.8, 'Converged?', kind='diamond', w=2.6, h=0.9)
    update= box(ax, 4.5, 4.0, 'Selection / crossover\nmutation, k = k+1')
    out   = box(ax, 4.5, 2.4, 'Output best solution', kind='parallelogram')
    end   = box(ax, 4.5, 1.0, 'End', kind='oval', w=2.0)
    arrow(ax, start, init); arrow(ax, init, evalb); arrow(ax, evalb, conv)
    arrow(ax, conv, update, label='No')
    arrow(ax, update, evalb, via=[(1.6, 4.0), (1.6, 7.4)])
    arrow(ax, conv, out, via=[(7.6, 5.8), (7.6, 2.4)], label='Yes')
    arrow(ax, out, end)
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
