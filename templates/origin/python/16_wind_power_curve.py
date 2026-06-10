"""16_wind_power_curve: 风机功率曲线（散点 + 设计曲线，对照 python 模板 v1.5）."""
import originpro as op
import numpy as np


def design_curve(v, v_in=3.0, v_rated=12.0, v_out=25.0):
    P = np.where(v < v_in, 0,
        np.where(v < v_rated, (v**3 - v_in**3)/(v_rated**3 - v_in**3),
        np.where(v < v_out, 1.0, 0.0)))
    return P


def make_power_curve(seed=0):
    rng = np.random.default_rng(seed)
    wb = op.new_book(lname='WindPC')
    wks = wb[0]
    vs = rng.uniform(0.5, 27, 220)
    Ps = np.clip(design_curve(vs) + rng.normal(0, 0.03, vs.size), 0, 1.08)
    v = np.linspace(0, 28, 200)
    wks.from_list(0, vs.tolist(), axis='X', lname='v_scada', units='m/s')
    wks.from_list(1, Ps.tolist(), axis='Y', lname='P_scada', units='p.u.')
    wks.from_list(2, v.tolist(), axis='X', lname='v_design', units='m/s')
    wks.from_list(3, design_curve(v).tolist(), axis='Y', lname='P_design', units='p.u.')
    gp = op.new_graph()
    gl = gp[0]
    gl.add_plot(wks, coly=1, colx=0, type='scatter')
    gl.add_plot(wks, coly=3, colx=2, type='line')
    gl.rescale()
    return gp


if __name__ == '__main__':
    gp = make_power_curve()
    print(f'created graph: {gp.name}')
