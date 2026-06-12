"""power_system_deep_cluster_view: 电力系统深化状态聚类散点（cluster 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='power system analysis: state cluster scatter'):
    return make_template_figure('scatter_cluster', seed=3605, title=title, domain='power system analysis', topic='state cluster scatter')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
