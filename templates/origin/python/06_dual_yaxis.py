"""06_dual_yaxis: 双 Y 轴（温度 + 湿度）."""
import originpro as op
import numpy as np

t = np.arange(24)
temp = 20 + 8*np.sin((t-6)*np.pi/12)
hum  = 60 - 20*np.sin((t-6)*np.pi/12)

wb = op.new_book(lname='Dual')
wks = wb[0]
wks.from_list(0, t.tolist(),    axis='X', lname='hour')
wks.from_list(1, temp.tolist(), axis='Y', lname='T',  units='C')
wks.from_list(2, hum.tolist(),  axis='Y', lname='RH', units='%')

gp = op.new_graph(template='doubleY', lname='DualY')

# 主层 = T
gp[0].add_plot(wks, '0,1', 'l')
gp[0].axis('y').title = 'Temperature (°C)'
# 副层 = RH
gp[1].add_plot(wks, '0,2', 'l')
gp[1].axis('y').title = 'Humidity (%)'

print('dual Y axis ready')
