"""paper_multipanel_before_after: 论文多面板版式前后斜率对比（slope 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='paper multipanel layout: before-after slope'):
    return make_template_figure('slope', seed=2220, title=title, domain='paper multipanel layout', topic='before-after slope')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
