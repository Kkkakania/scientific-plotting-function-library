"""pareto_front: 多目标优化 Pareto 前沿（Plotly 交互版，对应 templates/python/pareto_front.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(title='Pareto front') -> go.Figure:
    rng = np.random.default_rng(2)
    n = 400
    f1 = rng.uniform(0, 1, n)
    f2 = (1 - f1 ** 0.5) + 0.15 * rng.uniform(0, 1, n)
    # 找非支配点
    pareto = np.ones(n, dtype=bool)
    for i in range(n):
        for j in range(n):
            if (i != j and f1[j] <= f1[i] and f2[j] <= f2[i]
                    and (f1[j] < f1[i] or f2[j] < f2[i])):
                pareto[i] = False
                break
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=f1[~pareto], y=f2[~pareto], mode='markers', name='dominated',
        marker=dict(size=5, color='lightgray', opacity=0.7),
    ))
    order = np.argsort(f1[pareto])
    fig.add_trace(go.Scatter(
        x=f1[pareto][order], y=f2[pareto][order], mode='lines+markers',
        name='Pareto front',
        line=dict(color=COLORS[6], width=1),
        marker=dict(size=8, color=COLORS[6], line=dict(color='black', width=0.5)),
    ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='objective 1', yaxis_title='objective 2',
        legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'pareto_front.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
