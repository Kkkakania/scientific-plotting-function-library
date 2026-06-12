"""fluid_cfd_contribution_bridge: 流体与 CFD贡献瀑布桥（waterfall 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='fluid and CFD analysis: contribution waterfall'):
    return make_template_figure('waterfall', seed=2608, title=title, domain='fluid and CFD analysis', topic='contribution waterfall')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
