"""fluid_cfd_interval_forest: 流体与 CFD区间森林图（interval 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='fluid and CFD analysis: interval forest'):
    return make_template_figure('interval_forest', seed=2615, title=title, domain='fluid and CFD analysis', topic='interval forest')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
