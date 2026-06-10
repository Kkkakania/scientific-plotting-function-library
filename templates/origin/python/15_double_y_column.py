"""15_double_y_column: 柱状 + 折线双 Y 轴（实验量 vs 效率类组合图）."""
import originpro as op
import numpy as np


def make_double_y(seed=0):
    rng = np.random.default_rng(seed)
    wb = op.new_book(lname='DoubleY')
    wks = wb[0]
    x = list(range(1, 13))
    output = (50 + 8*np.sin(np.arange(12)/2) + rng.uniform(-3, 3, 12)).round(1)
    eff = (88 + 4*np.cos(np.arange(12)/3) + rng.uniform(-1, 1, 12)).round(2)
    wks.from_list(0, x, axis='X', lname='month')
    wks.from_list(1, output.tolist(), axis='Y', lname='output', units='MWh')
    wks.from_list(2, eff.tolist(), axis='Y', lname='efficiency', units='%')
    gp = op.new_graph(template='doubley')
    gp[0].add_plot(wks, coly=1, colx=0, type='column')
    gp[1].add_plot(wks, coly=2, colx=0, type='line')
    for gl in (gp[0], gp[1]):
        gl.rescale()
    return gp


if __name__ == '__main__':
    gp = make_double_y()
    print(f'created graph: {gp.name}')
