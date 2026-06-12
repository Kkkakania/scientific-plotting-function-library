"""education_diagram_decision_boundary: 教学图解决策边界图（decision-map 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='educational diagramming: decision boundary'):
    return make_template_figure('decision_map', seed=3221, title=title, domain='educational diagramming', topic='decision boundary')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
