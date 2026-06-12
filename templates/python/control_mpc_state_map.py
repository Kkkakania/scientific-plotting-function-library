"""control_mpc_state_map: MPC 控制进阶状态热力图（heatmap 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='advanced MPC control: state heatmap'):
    return make_template_figure('heatmap', seed=1603, title=title, domain='advanced MPC control', topic='state heatmap')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
