"""matrix_tensor_composition_stream: 矩阵与张量可视化组成流面积（stacked-area 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='matrix and tensor visualization: composition stream'):
    return make_template_figure('stacked_area', seed=4416, title=title, domain='matrix and tensor visualization', topic='composition stream')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
