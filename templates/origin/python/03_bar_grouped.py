"""03_bar_grouped: 分组柱状."""
import originpro as op
import numpy as np

rng = np.random.default_rng(2)
groups = ['A', 'B', 'C', 'D', 'E']
v1 = rng.uniform(10, 80, 5)
v2 = rng.uniform(10, 80, 5)
v3 = rng.uniform(10, 80, 5)

wb = op.new_book(lname='Bar')
wks = wb[0]
wks.from_list(0, groups, axis='X', lname='category')
wks.from_list(1, v1.tolist(), axis='Y', lname='2023')
wks.from_list(2, v2.tolist(), axis='Y', lname='2024')
wks.from_list(3, v3.tolist(), axis='Y', lname='2025')

gp = op.new_graph(template='bar', lname='GroupedBar')
gl = gp[0]
gl.add_plot(wks, '0,1', 'b')              # 'b' = bar
gl.add_plot(wks, '0,2', 'b')
gl.add_plot(wks, '0,3', 'b')
op.lt_exec('layer -g;')                   # 切换为分组模式

gl.axis('y').title = 'value'
gl.add_legend()
print('grouped bar ready')
