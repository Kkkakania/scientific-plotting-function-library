"""08_contour: 填充等高线（连续函数 z = f(x, y)）."""
import originpro as op
import numpy as np

n = 80
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)/2) - 0.5*np.exp(-((X-1.5)**2 + (Y-1.5)**2)/0.5)

mb = op.new_book('m', lname='ContourM')
ms = mb[0]
ms.xmin = x.min(); ms.xmax = x.max()
ms.ymin = y.min(); ms.ymax = y.max()
ms.from_np(Z.astype('float32'))

gp = op.new_graph(template='contour', lname='Contour')
gl = gp[0]
plt = gl.add_mplot(ms, 0, 'c')
plt.colormap = 'blue_white_red'           # 发散色
gl.axis('x').title = 'x'; gl.axis('y').title = 'y'
print('contour ready')
