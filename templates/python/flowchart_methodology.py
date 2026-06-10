"""flowchart_methodology: 论文研究方法流程图（线性主干 + 双列输入）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import matplotlib.pyplot as plt
from theme import apply_theme
from diagram import new_canvas, box, arrow, vflow

def make_figure(title='Research methodology'):
    apply_theme()
    fig, ax = new_canvas(10, 10)
    main = vflow(ax, 5, 9.2, [
        ('Problem definition', 'oval'),
        ('Data acquisition', 'box'),
        ('Preprocessing &\nfeature extraction', 'box'),
        ('Model training', 'box'),
        ('Validation & comparison', 'box'),
        ('Conclusions', 'oval')], gap=1.55, w=3.2)
    src1 = box(ax, 1.6, 7.65, 'Field\nmeasurements', kind='parallelogram', w=2.2)
    src2 = box(ax, 8.4, 7.65, 'Simulation\ndataset', kind='parallelogram', w=2.2)
    arrow(ax, src1, main[1]); arrow(ax, src2, main[1])
    crit = box(ax, 8.4, 3.0, 'Metrics:\nRMSE / MAE / R²', kind='process_alt', w=2.3)
    arrow(ax, crit, main[4])
    ax.set_title(title, fontsize=11)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
