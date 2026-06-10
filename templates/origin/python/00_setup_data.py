"""00_setup_data: 创建工作表 + 合成数据.

后面所有脚本都假设当前 Project 里至少有一张 'Demo' 工作簿。
"""
import originpro as op
import numpy as np


def setup_demo_data(seed=0):
    rng = np.random.default_rng(seed)
    wb = op.new_book(lname='Demo')
    wks = wb[0]
    wks.name = 'main'

    x = np.linspace(0, 10, 60)
    y1 = np.sin(x) + 0.08*rng.standard_normal(60)
    y2 = np.cos(x) + 0.08*rng.standard_normal(60)
    yerr = 0.05 + 0.05*rng.uniform(0, 1, 60)

    wks.from_list(0, x.tolist(),  axis='X', lname='X', units='s')
    wks.from_list(1, y1.tolist(), axis='Y', lname='sin', units='V')
    wks.from_list(2, y2.tolist(), axis='Y', lname='cos', units='V')
    wks.from_list(3, yerr.tolist(), axis='E', lname='err', comments='std')
    return wb


if __name__ == '__main__':
    wb = setup_demo_data()
    print(f'created workbook: {wb.name}')
