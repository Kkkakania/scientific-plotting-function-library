"""control_mpc_interaction_matrix: MPC 控制进阶交互气泡矩阵（matrix 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='advanced MPC control: interaction bubble matrix'):
    return make_template_figure('bubble_matrix', seed=1613, title=title, domain='advanced MPC control', topic='interaction bubble matrix')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
