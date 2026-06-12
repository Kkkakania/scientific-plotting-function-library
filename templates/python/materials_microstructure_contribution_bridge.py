"""materials_microstructure_contribution_bridge: 材料微结构贡献瀑布桥（waterfall 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='materials microstructure: contribution waterfall'):
    return make_template_figure('waterfall', seed=1808, title=title, domain='materials microstructure', topic='contribution waterfall')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
