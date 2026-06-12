"""logistics_network_response_surface: 物流与网络响应等值面（contour 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='logistics and network analysis: response contour surface'):
    return make_template_figure('contour', seed=3404, title=title, domain='logistics and network analysis', topic='response contour surface')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
