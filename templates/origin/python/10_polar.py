"""10_polar: 极坐标曲线."""
import originpro as op
import numpy as np

theta = np.linspace(0, 360, 360)         # 角度（度）
r = 1 + 0.6*np.sin(np.deg2rad(5*theta))

wb = op.new_book(lname='PolarData')
wks = wb[0]
wks.from_list(0, theta.tolist(), axis='X', lname='theta (deg)')
wks.from_list(1, r.tolist(),     axis='Y', lname='r')

gp = op.new_graph(template='polar', lname='Polar')
gp[0].add_plot(wks, '0,1', 'l')
print('polar plot ready')
