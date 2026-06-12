"""matrix_tensor_scenario_facets: 矩阵与张量可视化场景分面（small-multiples 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='matrix and tensor visualization: scenario small multiples'):
    return make_template_figure('small_multiples', seed=4409, title=title, domain='matrix and tensor visualization', topic='scenario small multiples')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
