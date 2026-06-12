"""matrix_tensor_decision_boundary: 矩阵与张量可视化决策边界图（decision-map 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='matrix and tensor visualization: decision boundary'):
    return make_template_figure('decision_map', seed=4421, title=title, domain='matrix and tensor visualization', topic='decision boundary')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
