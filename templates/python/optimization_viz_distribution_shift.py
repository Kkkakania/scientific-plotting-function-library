"""optimization_viz_distribution_shift: 优化算法可视化分布漂移（distribution 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='optimization visualization: distribution shift'):
    return make_template_figure('distribution', seed=2912, title=title, domain='optimization visualization', topic='distribution shift')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
