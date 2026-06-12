"""fluid_cfd_stage_step: 流体与 CFD阶段阶梯曲线（step 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='fluid and CFD analysis: stage step curve'):
    return make_template_figure('step_curve', seed=2617, title=title, domain='fluid and CFD analysis', topic='stage step curve')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
