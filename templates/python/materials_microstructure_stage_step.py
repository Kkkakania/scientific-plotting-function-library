"""materials_microstructure_stage_step: 材料微结构阶段阶梯曲线（step 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='materials microstructure: stage step curve'):
    return make_template_figure('step_curve', seed=1817, title=title, domain='materials microstructure', topic='stage step curve')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
