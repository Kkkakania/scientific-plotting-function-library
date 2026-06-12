"""bio_signal_calendar_grid: 生物信号日历网格（calendar-grid 模式，合成数据）."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='biomedical signal analysis: calendar grid'):
    return make_template_figure('calendar_grid', seed=2719, title=title, domain='biomedical signal analysis', topic='calendar grid')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
