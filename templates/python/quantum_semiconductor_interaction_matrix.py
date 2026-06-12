"""quantum_semiconductor_interaction_matrix: 量子与半导体交互气泡矩阵（matrix 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='quantum and semiconductor analysis: interaction bubble matrix'):
    return make_template_figure('bubble_matrix', seed=3013, title=title, domain='quantum and semiconductor analysis', topic='interaction bubble matrix')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
