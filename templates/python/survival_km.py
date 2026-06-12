"""survival_km: Kaplan-Meier 生存曲线（两组 + 删失标记 + 风险人数表）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme
from palette import cycle

def _km(t, event):
    order = np.argsort(t)
    t, event = t[order], event[order]
    n = len(t)
    at_risk = n - np.arange(n)
    s = np.cumprod(1.0 - event / at_risk)
    return np.concatenate([[0], t]), np.concatenate([[1.0], s]), t, event, s

def make_figure(title='Kaplan-Meier survival'):
    apply_theme()
    rng = np.random.default_rng(3)
    groups = []
    for scale, n in [(18.0, 60), (10.0, 60)]:
        true_t = rng.exponential(scale, n)
        cens_t = rng.uniform(5, 24, n)
        t = np.minimum(true_t, cens_t)
        event = (true_t <= cens_t).astype(float)
        groups.append((t, event))
    fig, (ax, axt) = plt.subplots(2, 1, figsize=(6, 5.2), sharex=True,
                                  gridspec_kw={'height_ratios': [4, 1]})
    marks = np.arange(0, 25, 6)
    for i, ((t, ev), name) in enumerate(zip(groups, ['Treatment', 'Control'])):
        ts, ss, tt, evt, sv = _km(t, ev)
        ax.step(ts, ss, where='post', color=cycle(i), label=name)
        cmask = evt == 0
        ax.plot(tt[cmask], sv[cmask], '|', color=cycle(i), markersize=7,
                markeredgewidth=1.2)
        n_risk = [(t >= m).sum() for m in marks]
        for m, nr in zip(marks, n_risk):
            axt.text(m, 0.66 - 0.38*i, str(nr), ha='center', va='center',
                     fontsize=8, color=cycle(i))
        axt.text(-1.2, 0.66 - 0.38*i, name, ha='right', va='center',
                 fontsize=8, color=cycle(i))
    ax.set_ylabel('survival probability'); ax.set_ylim(0, 1.04)
    ax.set_title(title)
    ax.legend(loc='upper right'); ax.grid(True, linestyle=':', alpha=0.5)
    axt.set_ylim(0, 1); axt.set_yticks([])
    axt.set_xlabel('time (months)')
    axt.set_ylabel('at risk', fontsize=8)
    axt.spines['left'].set_visible(False)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
