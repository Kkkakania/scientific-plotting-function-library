"""17_harmonic_spectrum: 谐波频谱柱状（电气，对照 python/harmonic_spectrum.py）."""
import originpro as op
import numpy as np


def make_harmonics(seed=0):
    rng = np.random.default_rng(seed)
    wb = op.new_book(lname='Harmonics')
    wks = wb[0]
    orders = np.arange(1, 26)
    amps = np.zeros(25); amps[0] = 1.0
    amps[[2, 4, 6, 10]] = [0.3, 0.18, 0.08, 0.05]
    amps += rng.uniform(0, 0.02, 25)
    wks.from_list(0, orders.tolist(), axis='X', lname='harmonic order')
    wks.from_list(1, (amps*100).tolist(), axis='Y', lname='amplitude', units='% of fund.')
    gp = op.new_graph()
    gl = gp[0]
    gl.add_plot(wks, coly=1, colx=0, type='column')
    gl.rescale()
    return gp


if __name__ == '__main__':
    gp = make_harmonics()
    print(f'created graph: {gp.name}')
