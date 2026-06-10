"""shap_summary: SHAP 摘要图（蜂群形式）."""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
import numpy as np
import matplotlib.pyplot as plt
from theme import apply_theme

def make_figure(title='SHAP summary'):
    apply_theme(fig_size=(7, 5))
    rng = np.random.default_rng(9)
    n_feat = 8; n = 200
    feat_imp_order = rng.normal(0, 1, (n_feat, n))
    feat_imp_order = feat_imp_order[np.argsort(np.abs(feat_imp_order).mean(1))[::-1]]
    feat_val = rng.uniform(0, 1, (n_feat, n))
    fig, ax = plt.subplots()
    for i in range(n_feat):
        y = i + 0.3*rng.uniform(-1, 1, n)
        sc = ax.scatter(feat_imp_order[i], y, c=feat_val[i], cmap='coolwarm',
                        s=15, alpha=0.8, edgecolors='none')
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_yticks(range(n_feat))
    ax.set_yticklabels([f'feat_{i+1}' for i in range(n_feat)])
    ax.invert_yaxis()
    ax.set_xlabel('SHAP value (impact on output)')
    ax.set_title(title)
    fig.colorbar(sc, ax=ax, label='feature value', shrink=0.7)
    fig.tight_layout()
    return fig

if __name__ == '__main__':
    fig = make_figure(); fig.savefig(__file__.replace('.py', '.png'), dpi=150)
