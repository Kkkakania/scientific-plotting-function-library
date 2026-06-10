"""07_heatmap: 矩阵热力图."""
import originpro as op
import numpy as np

rng = np.random.default_rng(5)
M = rng.uniform(0, 1, (8, 12))

# 用 MatrixBook（Origin 热力图通常以矩阵为输入）
mb = op.new_book('m', lname='HeatM')
ms = mb[0]
ms.from_np(M.astype('float32'))

gp = op.new_graph(template='contour', lname='Heatmap')
gl = gp[0]
plt = gl.add_mplot(ms, 0, 'c')             # 'c' = contour / heatmap
plt.colormap = 'blues'                     # Origin 内置色系名
gl.axis('x').title = 'column'
gl.axis('y').title = 'row'
print('heatmap ready')
