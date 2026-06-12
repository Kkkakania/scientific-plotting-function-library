"""motor_deep_cluster_view: 电机深化状态聚类散点（cluster 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='electric motor analysis: state cluster scatter'):
    return make_template_figure('scatter_cluster', seed=2305, title=title, domain='electric motor analysis', topic='state cluster scatter')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
