"""thermal_system_scenario_facets: 热学系统场景分面（small-multiples 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='thermal system analysis: scenario small multiples'):
    return make_template_figure('small_multiples', seed=2509, title=title, domain='thermal system analysis', topic='scenario small multiples')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
