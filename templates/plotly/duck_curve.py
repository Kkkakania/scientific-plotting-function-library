"""duck_curve: 净负荷鸭子曲线（光伏渗透率逐年上升，Plotly 交互版，对应 templates/python/duck_curve.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
import sci_palettes


def _sample_seq(name, frac):
    """在库内顺序色板（RGB 0-1 浮点元组列表）上线性插值取色，frac ∈ [0, 1]."""
    cols = sci_palettes.PALETTES_SEQ[name]
    pos = frac * (len(cols) - 1)
    i = min(int(pos), len(cols) - 2)
    t = pos - i
    rgb = [round((cols[i][k] * (1 - t) + cols[i + 1][k] * t) * 255)
           for k in range(3)]
    return 'rgb({},{},{})'.format(*rgb)


def make_figure(title='Duck curve: net load vs PV penetration') -> go.Figure:
    t = np.linspace(0, 24, 480)
    load = (20 + 6 * np.exp(-0.5 * ((t - 9) / 2.6) ** 2)
            + 9 * np.exp(-0.5 * ((t - 19.5) / 2.0) ** 2))
    pv_shape = np.exp(-0.5 * ((t - 12.5) / 2.7) ** 2) * (np.abs(t - 12.5) < 7)
    years = [2018, 2020, 2022, 2024, 2026]
    fig = go.Figure()
    for i, yr in enumerate(years):
        net = load - (2.2 * i) * pv_shape
        fig.add_trace(go.Scatter(
            x=t, y=net, mode='lines', name=str(yr),
            line=dict(color=_sample_seq('blues', 0.25 + 0.75 * i / (len(years) - 1)),
                      width=2),
        ))
    fig.add_annotation(x=16.6, y=17, ax=12.6, ay=12.5,
                       axref='x', ayref='y', text='growing ramp',
                       showarrow=True, arrowhead=2, font=dict(size=10))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='hour of day', yaxis_title='net load (GW)',
        xaxis_range=[0, 24], legend=dict(title='year', borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'duck_curve.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
