"""02_scatter: 散点 + 线性回归 + 95% 置信带."""
import originpro as op
import numpy as np

rng = np.random.default_rng(1)
n = 80
x = rng.uniform(0, 10, n)
y = 1.5*x + 2 + 1.5*rng.standard_normal(n)

wb = op.new_book(lname='Scatter')
wks = wb[0]
wks.from_list(0, x.tolist(), axis='X')
wks.from_list(1, y.tolist(), axis='Y')

gp = op.new_graph(template='scatter', lname='ScatterFit')
gl = gp[0]
plt = gl.add_plot(wks, '0,1', 's')        # 's' = 散点
plt.color = '#4C72B0'

# 用 LabTalk 触发 Origin 自带的线性拟合
op.lt_exec('linearFit -i 1;')
op.lt_exec('run.section(LR, Main, x:= col(1) y:= col(2));')

gl.axis('x').title = 'x'
gl.axis('y').title = 'y'
print('scatter + fit ready')
