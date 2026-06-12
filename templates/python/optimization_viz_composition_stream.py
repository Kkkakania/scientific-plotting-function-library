"""optimization_viz_composition_stream: 优化算法可视化组成流面积（stacked-area 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='optimization visualization: composition stream'):
    return make_template_figure('stacked_area', seed=2916, title=title, domain='optimization visualization', topic='composition stream')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
