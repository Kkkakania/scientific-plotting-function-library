"""01_line_plot: 双线折线图，论文风格."""
import originpro as op

# 假设已有 Demo 工作簿（运行 00 后）
wks = op.find_sheet('w', '[Demo]main')

gp = op.new_graph(template='line', lname='LinePlot')
gl = gp[0]

p1 = gl.add_plot(wks, '0,1', 'l')      # 类型 'l' = 折线
p2 = gl.add_plot(wks, '0,2', 'l')
p1.color = '#0072B2'; p1.set_int('linewidth', 2)
p2.color = '#D55E00'; p2.set_int('linewidth', 2); p2.set_int('linetype', 2)  # 虚线

gl.rescale()
gl.axis('x').title = 't (s)'
gl.axis('y').title = 'amplitude (V)'
gl.add_legend()

print('line plot ready in Origin')
