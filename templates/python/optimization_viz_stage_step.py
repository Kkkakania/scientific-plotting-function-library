"""optimization_viz_stage_step: 优化算法可视化阶段阶梯曲线（step 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='optimization visualization: stage step curve'):
    return make_template_figure('step_curve', seed=2917, title=title, domain='optimization visualization', topic='stage step curve')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
