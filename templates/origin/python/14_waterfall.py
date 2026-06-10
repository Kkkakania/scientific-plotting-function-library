"""14_waterfall: 瀑布图（多条谱线按 Z 偏移堆叠，光谱/时变频谱常用）."""
import originpro as op
import numpy as np


def make_waterfall(n_curves=8, seed=0):
    rng = np.random.default_rng(seed)
    wb = op.new_book(lname='Waterfall')
    wks = wb[0]
    x = np.linspace(400, 800, 200)            # 波长 nm
    wks.from_list(0, x.tolist(), axis='X', lname='wavelength', units='nm')
    for i in range(n_curves):
        peak = 520 + i*18
        y = np.exp(-0.5*((x - peak)/22)**2)*(1 - i*0.06) \
            + 0.02*rng.standard_normal(x.size)
        wks.from_list(1 + i, y.tolist(), axis='Y', lname=f't={i*5} min')
    gp = op.new_graph(template='waterfall')
    gl = gp[0]
    gl.add_plot(wks, coly=list(range(1, 1 + n_curves)), colx=0, type='line')
    gl.rescale()
    return gp


if __name__ == '__main__':
    gp = make_waterfall()
    print(f'created graph: {gp.name}')
