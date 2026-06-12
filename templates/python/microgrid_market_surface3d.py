"""microgrid_market_surface3d: 微电网与市场三维响应曲面（3d-surface 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='microgrid and market analysis: 3D response surface'):
    return make_template_figure('surface3d', seed=3818, title=title, domain='microgrid and market analysis', topic='3D response surface')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
