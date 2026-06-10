"""heatmap_basic: 基础热力图（Plotly 交互版，对应 templates/python/heatmap_basic.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
import sci_palettes


def _seq_colorscale(name='blues'):
    """把库内顺序色板（RGB 0-1 浮点元组列表）转为 Plotly colorscale."""
    cols = sci_palettes.PALETTES_SEQ[name]
    n = len(cols)
    return [[i / (n - 1), 'rgb({},{},{})'.format(*(round(v * 255) for v in c))]
            for i, c in enumerate(cols)]


def make_figure(M=None, title='Heatmap') -> go.Figure:
    if M is None:
        rng = np.random.default_rng(0)
        M = rng.uniform(0, 1, (8, 12))
    fig = go.Figure(go.Heatmap(
        z=M, colorscale=_seq_colorscale('blues'),
        colorbar=dict(title='value', outlinewidth=0),
    ))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='column', yaxis_title='row',
        legend=dict(borderwidth=0),
    )
    fig.update_yaxes(autorange='reversed')  # 与 imshow 行序一致
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'heatmap_basic.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
