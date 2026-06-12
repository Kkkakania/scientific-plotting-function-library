"""fluid_cfd_before_after: 流体与 CFD前后斜率对比（slope 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='fluid and CFD analysis: before-after slope'):
    return make_template_figure('slope', seed=2620, title=title, domain='fluid and CFD analysis', topic='before-after slope')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
