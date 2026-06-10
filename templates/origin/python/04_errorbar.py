"""04_errorbar: 折线 + 误差棒."""
import originpro as op
import numpy as np

rng = np.random.default_rng(3)
x = np.arange(1, 11)
y = 2 + np.log(x) + 0.1*rng.standard_normal(10)
err = 0.1 + 0.2*rng.uniform(0, 1, 10)

wb = op.new_book(lname='ErrPlot')
wks = wb[0]
wks.from_list(0, x.tolist(),   axis='X')
wks.from_list(1, y.tolist(),   axis='Y')
wks.from_list(2, err.tolist(), axis='E', lname='±err')

gp = op.new_graph(template='line+symbol', lname='ErrorPlot')
gl = gp[0]
gl.add_plot(wks, '0,1,2', 'y')           # 'y' = errorbar
gl.axis('x').title = 'x'
gl.axis('y').title = 'y ± err'
print('errorbar ready')
