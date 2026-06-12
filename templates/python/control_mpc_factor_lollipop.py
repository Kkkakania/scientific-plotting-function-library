"""control_mpc_factor_lollipop: MPC 控制进阶因子棒棒糖（lollipop 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='advanced MPC control: factor lollipop'):
    return make_template_figure('lollipop', seed=1614, title=title, domain='advanced MPC control', topic='factor lollipop')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
