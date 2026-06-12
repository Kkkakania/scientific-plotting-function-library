"""observer_estimation_state_map: 观测器与状态估计状态热力图（heatmap 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='observer and state estimation: state heatmap'):
    return make_template_figure('heatmap', seed=1703, title=title, domain='observer and state estimation', topic='state heatmap')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
