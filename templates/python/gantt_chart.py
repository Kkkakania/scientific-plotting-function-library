"""gantt_chart: 甘特图（8 任务依赖箭头 + 今日线 + 完成度填充）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def make_figure(title='Project Gantt chart'):
    apply_theme(fig_size=(8, 4.2))
    # (任务名, 开始日, 工期, 完成度, 前置任务索引或 None)
    tasks = [('Requirements',  0, 10, 1.00, None),
             ('System design', 8, 12, 1.00, 0),
             ('Prototype',    18, 14, 0.80, 1),
             ('Procurement',  14, 18, 0.65, 1),
             ('Implementation', 30, 20, 0.35, 2),
             ('Integration',  44, 12, 0.10, 4),
             ('Validation',   52, 14, 0.00, 5),
             ('Documentation', 40, 24, 0.20, 3)]
    today = 38
    fig, ax = plt.subplots()
    for i, (name, s, d, frac, dep) in enumerate(tasks):
        ax.barh(i, d, left=s, height=0.55, color=cycle(i % 4), alpha=0.30)
        ax.barh(i, d * frac, left=s, height=0.55, color=cycle(i % 4))
        ax.text(s + d + 0.6, i, f'{frac*100:.0f}%', va='center', fontsize=7)
        if dep is not None:
            ps, pd = tasks[dep][1], tasks[dep][2]
            ax.annotate('', xy=(s, i - 0.28), xytext=(ps + pd, dep),
                        arrowprops=dict(arrowstyle='->', color='#777777',
                                        linewidth=0.9,
                                        connectionstyle='angle,angleA=0,angleB=90'))
    ax.axvline(today, color=cycle(1), linestyle='--', linewidth=1.2)
    ax.text(today, len(tasks) - 0.2, ' today', color=cycle(1), fontsize=8)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([t[0] for t in tasks])
    ax.invert_yaxis()
    ax.set_xlabel('project day'); ax.set_ylabel('task'); ax.set_title(title)
    ax.grid(True, axis='x', linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
