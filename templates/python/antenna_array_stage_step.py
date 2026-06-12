"""antenna_array_stage_step: 天线阵列阶段阶梯曲线（step 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='antenna array analysis: stage step curve'):
    return make_template_figure('step_curve', seed=4217, title=title, domain='antenna array analysis', topic='stage step curve')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
