"""09_3d_surface: 三维曲面."""
import originpro as op
import numpy as np

n = 60
x = np.linspace(-8, 8, n)
y = np.linspace(-8, 8, n)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2) + 1e-9
Z = np.sin(R) / R

mb = op.new_book('m', lname='SurfM')
ms = mb[0]
ms.xmin = x.min(); ms.xmax = x.max()
ms.ymin = y.min(); ms.ymax = y.max()
ms.from_np(Z.astype('float32'))

gp = op.new_graph(template='surface', lname='Surface3D')
gl = gp[0]
plt = gl.add_mplot(ms, 0, 's')             # 's' here = surface (template-specific)
plt.colormap = 'turbo_like'
gl.axis('x').title = 'x'; gl.axis('y').title = 'y'
print('3D surface ready')
