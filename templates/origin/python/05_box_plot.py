"""05_box_plot: 箱线图（4 组数据）."""
import originpro as op
import numpy as np

rng = np.random.default_rng(4)
groups = [rng.normal(loc, 1, 50) for loc in [0, 1, 2, 1.5]]

wb = op.new_book(lname='BoxData')
wks = wb[0]
for i, arr in enumerate(groups):
    wks.from_list(i, arr.tolist(), axis='Y', lname=chr(ord('A')+i))

gp = op.new_graph(template='box', lname='BoxPlot')
gl = gp[0]
gl.add_plot(wks, '0,1,2,3', 'box')        # 'box' = box plot
gl.axis('x').title = 'group'
gl.axis('y').title = 'value'
print('box plot ready')
