"""logistics_network_rank_profile: 物流与网络指标排序条形（ranking 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='logistics and network analysis: ranked metric profile'):
    return make_template_figure('rank_bar', seed=3406, title=title, domain='logistics and network analysis', topic='ranked metric profile')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
