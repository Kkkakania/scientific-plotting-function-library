"""pv_mismatch_iv: 光伏阵列失配 I-V（3 并联支路部分遮挡，旁路二极管致阵列 P-V 多峰）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _substring_v(i, iph, i0=7e-8, n_vt=0.0334, ns=18, v_bypass=-0.6):
    """单二极管模型子串电压: V = Ns*n*Vt*ln((Iph-I)/I0 + 1), I>Iph 时旁路二极管钳位."""
    arg = np.maximum((iph - i) / i0 + 1.0, 1e-12)
    v = ns * n_vt * np.log(arg)
    return np.where(i < iph, v, v_bypass)

def make_figure(title='PV array I-V under partial shading'):
    """阵列结构: 3 条支路并联, 每条 = 2 个带旁路二极管的子串(18 cell)串联。
    遮挡情况: 支路1 无遮挡 (Iph=8/8 A), 支路2 半串遮挡 50% (8/4 A),
    支路3 半串遮挡 75% (8/2 A)。遮挡子串被旁路 → 支路 I-V 出现台阶,
    并联合成后阵列 P-V 呈多峰 (全局/局部 MPP)。
    """
    apply_theme()
    iph_pairs = [(8.0, 8.0), (8.0, 4.0), (8.0, 2.0)]
    labels = ['String 1 (no shading)', 'String 2 (50% shaded half)',
              'String 3 (75% shaded half)']
    # 电流网格在各 Iph 附近加密, 以解析二极管膝点处的陡降 (V → 0)
    i = np.sort(np.concatenate(
        [np.linspace(0.0, 8.05, 600)] +
        [iph - np.logspace(-8, -0.3, 80) for iph in (2.0, 4.0, 8.0)]))
    v_grid = np.linspace(0.0, 24.0, 800)
    i_array = np.zeros_like(v_grid)
    fig, ax = plt.subplots()
    for k, ((iph1, iph2), lab) in enumerate(zip(iph_pairs, labels)):
        v_str = _substring_v(i, iph1) + _substring_v(i, iph2)
        m = v_str >= 0                                       # 只保留发电象限
        ax.plot(v_str[m], i[m], color=cycle(k), linewidth=1.2, label=lab)
        # 支路电流按电压插值后并联相加 (V 同, I 相加)
        v_sorted = v_str[m][::-1]; i_sorted = i[m][::-1]
        i_array += np.interp(v_grid, v_sorted, i_sorted,
                             left=i_sorted[0], right=0.0)
    ax.plot(v_grid, i_array, color=cycle(3), linewidth=2.0, label='Array (parallel)')
    ax2 = ax.twinx()                                          # 阵列功率显示多峰
    p = v_grid * i_array
    ax2.plot(v_grid, p, color=cycle(7), linestyle='--', linewidth=1.2,
             label='Array power')
    ax2.set_ylabel('array power (W)')
    ax2.set_ylim(0, p.max() * 1.30)
    ax2.spines['right'].set_visible(True)
    ax.set_xlabel('voltage (V)'); ax.set_ylabel('current (A)')
    ax.set_title(title)
    ax.set_xlim(0, 24); ax.set_ylim(0, 26)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, frameon=False, loc='upper left', fontsize=7)
    ax.grid(True, linestyle=':', alpha=0.5)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
