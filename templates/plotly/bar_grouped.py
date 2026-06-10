"""bar_grouped: 分组柱状（多系列并排，Plotly 交互版，对应 templates/python/bar_grouped.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(labels=None, V=None, series_names=None, title='Grouped bar') -> go.Figure:
    if labels is None:
        rng = np.random.default_rng(0)
        n_cat, n_series = 5, 3
        labels = [f'cat{i + 1}' for i in range(n_cat)]
        V = rng.uniform(10, 80, (n_series, n_cat))
        series_names = ['2023', '2024', '2025']
    fig = go.Figure()
    for i, row in enumerate(V):
        fig.add_trace(go.Bar(
            x=labels, y=row,
            name=series_names[i] if series_names else f'series {i + 1}',
            marker_color=COLORS[i % len(COLORS)],
        ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12), barmode='group',
        title=title, xaxis_title='category', yaxis_title='value',
        legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'bar_grouped.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
