"""education_diagram_state_map: 教学图解状态热力图（heatmap 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='educational diagramming: state heatmap'):
    return make_template_figure('heatmap', seed=3203, title=title, domain='educational diagramming', topic='state heatmap')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
