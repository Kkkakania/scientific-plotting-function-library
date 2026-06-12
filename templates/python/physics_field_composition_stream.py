"""physics_field_composition_stream: 物理场分析组成流面积（stacked-area 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='physics field analysis: composition stream'):
    return make_template_figure('stacked_area', seed=2016, title=title, domain='physics field analysis', topic='composition stream')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
