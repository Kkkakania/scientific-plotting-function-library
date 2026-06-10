"""11_multi_panel: 2×2 多面板（论文级 a/b/c/d 标号）."""
import originpro as op
import numpy as np

rng = np.random.default_rng(6)
wb = op.new_book(lname='Panels')
wks = wb[0]
x = np.linspace(0, 10, 100)
wks.from_list(0, x.tolist(), axis='X')
for k in range(1, 5):
    wks.from_list(k, (np.sin(k*x) + 0.05*rng.standard_normal(100)).tolist(),
                  axis='Y', lname=f'series{k}')

# 用 PAN2 模板（Origin 自带 2×2 panel 模板）
gp = op.new_graph(template='PAN2', lname='MultiPanel')

for i in range(4):
    gp[i].add_plot(wks, f'0,{i+1}', 'l')
    gp[i].add_label(f'({chr(ord("a")+i)})', x=0.05, y=0.93,
                    fontsize=12, bold=True)
print('multi-panel ready')
