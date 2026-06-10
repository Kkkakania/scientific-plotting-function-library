"""wind_power_curve: 风机功率曲线（理论曲线 + 实测散点，Plotly 交互版，对应 templates/python/wind_power_curve.py）."""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', 'palettes', 'python'))

import numpy as np
import plotly.graph_objects as go
from sci_palettes import get_palette

COLORS = get_palette('wong')


def make_figure(v_in=3.0, v_rated=12.0, v_out=25.0,
                title='Wind turbine power curve') -> go.Figure:
    rng = np.random.default_rng(0)
    v = np.linspace(0, 28, 400)
    P = np.where(v < v_in, 0,
        np.where(v < v_rated, (v ** 3 - v_in ** 3) / (v_rated ** 3 - v_in ** 3),
        np.where(v < v_out, 1.0, 0.0)))
    vs = rng.uniform(0.5, 27, 220)
    Ps = np.interp(vs, v, P) + rng.normal(0, 0.03, vs.size)
    Ps = np.clip(Ps + (vs > v_in) * rng.normal(0, 0.02, vs.size), 0, 1.08)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=vs, y=Ps, mode='markers', name='SCADA data',
        marker=dict(size=5, color=COLORS[5], opacity=0.45),
    ))
    fig.add_trace(go.Scatter(
        x=v, y=P, mode='lines', name='design curve',
        line=dict(color=COLORS[6], width=2.5),
    ))
    for x0, lab in [(v_in, 'cut-in'), (v_rated, 'rated'), (v_out, 'cut-out')]:
        fig.add_vline(x=x0, line=dict(color='gray', dash='dot', width=1))
        fig.add_annotation(x=x0, y=1.12, text=lab, showarrow=False,
                           font=dict(size=10))
    fig.update_layout(
        template='plotly_white', font=dict(size=12),
        title=title, xaxis_title='wind speed (m/s)', yaxis_title='power (p.u.)',
        yaxis_range=[-0.04, 1.18], legend=dict(borderwidth=0),
    )
    return fig


if __name__ == '__main__':
    fig = make_figure()
    out = os.path.join(_HERE, 'wind_power_curve.html')
    fig.write_html(out, include_plotlyjs='cdn')
    print('written', out)
