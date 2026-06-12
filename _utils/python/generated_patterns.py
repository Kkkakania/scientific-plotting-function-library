"""Reusable clean-room pattern renderer for large template expansion.

The wrappers in templates/python pass only a semantic domain, topic, seed and
pattern kind. Synthetic data is generated here so the public templates remain
auditable and compact.
"""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from palette import cycle, diverging, sequential
from theme import apply_theme


def _rng(seed: int) -> np.random.Generator:
    return np.random.default_rng(seed)


def _series(seed: int, n: int = 96, k: int = 3):
    rng = _rng(seed)
    x = np.arange(n)
    base = np.cumsum(rng.normal(0, 0.12, n)) + np.sin(np.linspace(0, 5.8, n))
    ys = []
    for i in range(k):
        drift = 0.015 * (i - 1) * x
        seasonal = 0.25 * np.sin(np.linspace(0, 4 * np.pi, n) + i * 0.6)
        ys.append(base + drift + seasonal + rng.normal(0, 0.08 + 0.02 * i, n))
    return x, np.vstack(ys)


def _labels(prefix: str, n: int) -> list[str]:
    return [f"{prefix} {i + 1}" for i in range(n)]


def make_template_figure(kind: str, *, seed: int, title: str, domain: str, topic: str):
    """Render one deterministic publication-style figure."""
    kind = kind.lower()
    apply_theme(font_size=8.5, fig_size=(6.4, 4.2))

    if kind == "band_timeseries":
        x, y = _series(seed, 120, 1)
        y = y[0]
        width = np.linspace(0.25, 0.85, x.size)
        fig, ax = plt.subplots()
        ax.fill_between(x, y - width, y + width, color=cycle(seed), alpha=0.18, label="expected range")
        ax.plot(x, y, color=cycle(seed + 1), label=topic)
        ax.set_xlabel("sample"); ax.set_ylabel("value"); ax.legend()

    elif kind == "control_limit":
        x, y = _series(seed, 100, 1)
        y = y[0] + np.linspace(0, 1.2, x.size) * (seed % 3 == 0)
        center, sigma = np.mean(y[:35]), np.std(y[:35])
        fig, ax = plt.subplots()
        ax.plot(x, y, color=cycle(0), marker="o", ms=2.4)
        for m, ls in [(0, "-"), (2, "--"), (-2, "--"), (3, ":"), (-3, ":")]:
            ax.axhline(center + m * sigma, color=cycle(1 if abs(m) == 3 else 7), lw=1, ls=ls)
        ax.scatter(x[np.abs(y - center) > 3 * sigma], y[np.abs(y - center) > 3 * sigma],
                   color=cycle(1), zorder=4, label="out of control")
        ax.set_xlabel("sample"); ax.set_ylabel("statistic"); ax.legend()

    elif kind == "heatmap":
        rng = _rng(seed)
        rows, cols = 9, 12
        r = np.linspace(-1, 1, rows)[:, None]
        c = np.linspace(-1, 1, cols)[None, :]
        z = np.exp(-2.8 * ((r - 0.25) ** 2 + (c + 0.15) ** 2)) + 0.25 * rng.normal(size=(rows, cols))
        fig, ax = plt.subplots()
        im = ax.imshow(z, cmap=sequential("blue"), aspect="auto")
        fig.colorbar(im, ax=ax, shrink=0.82)
        ax.set_xlabel("condition"); ax.set_ylabel("channel")

    elif kind == "contour":
        x = np.linspace(-3, 3, 90)
        y = np.linspace(-2.5, 2.5, 80)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X * (1 + seed % 5 / 8)) * np.cos(Y) + 0.25 * X - 0.12 * Y**2
        fig, ax = plt.subplots()
        cs = ax.contourf(X, Y, Z, levels=14, cmap=diverging())
        ax.contour(X, Y, Z, levels=8, colors="k", linewidths=0.35, alpha=0.45)
        fig.colorbar(cs, ax=ax, shrink=0.82)
        ax.set_xlabel("x"); ax.set_ylabel("y")

    elif kind == "scatter_cluster":
        rng = _rng(seed)
        fig, ax = plt.subplots()
        for i in range(4):
            mean = np.array([np.cos(i * 1.6), np.sin(i * 1.6)]) * (1.2 + 0.1 * i)
            pts = rng.normal(size=(55, 2)) @ np.array([[0.22, 0.06], [0.02, 0.36]]) + mean
            ax.scatter(pts[:, 0], pts[:, 1], s=18, color=cycle(i), alpha=0.78, label=f"state {i+1}")
        ax.set_xlabel("feature 1"); ax.set_ylabel("feature 2"); ax.legend(ncol=2)

    elif kind == "rank_bar":
        rng = _rng(seed)
        values = np.sort(rng.lognormal(mean=0.0, sigma=0.45, size=8))[::-1]
        labels = _labels("item", len(values))
        fig, ax = plt.subplots()
        ax.barh(np.arange(len(values)), values, color=[cycle(i) for i in range(len(values))])
        ax.set_yticks(np.arange(len(values)), labels)
        ax.invert_yaxis(); ax.set_xlabel("score")

    elif kind == "radar":
        rng = _rng(seed)
        n = 6
        theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
        vals = 0.45 + 0.45 * rng.random((3, n))
        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        for i, row in enumerate(vals):
            v = np.r_[row, row[0]]
            th = np.r_[theta, theta[0]]
            ax.plot(th, v, color=cycle(i), label=f"case {i+1}")
            ax.fill(th, v, color=cycle(i), alpha=0.08)
        ax.set_xticks(theta, _labels("M", n)); ax.set_ylim(0, 1.0); ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.15))

    elif kind == "waterfall":
        rng = _rng(seed)
        steps = rng.normal(0.15, 0.75, 10)
        cum = np.r_[0, np.cumsum(steps)]
        fig, ax = plt.subplots()
        for i, step in enumerate(steps):
            bottom = min(cum[i], cum[i + 1])
            ax.bar(i, abs(step), bottom=bottom, width=0.65, color=cycle(2 if step >= 0 else 1))
            ax.plot([i - 0.32, i + 0.32], [cum[i + 1], cum[i + 1]], color="0.35", lw=0.8)
        ax.axhline(0, color="0.25", lw=0.8)
        ax.set_xlabel("step"); ax.set_ylabel("cumulative change")

    elif kind == "small_multiples":
        x, y = _series(seed, 72, 6)
        fig, axs = plt.subplots(2, 3, sharex=True, sharey=True)
        for i, ax in enumerate(axs.flat):
            ax.plot(x, y[i], color=cycle(i))
            ax.axhline(np.mean(y[i]), color="0.45", lw=0.6, ls=":")
            ax.set_title(f"scenario {i+1}", fontsize=8)
        fig.supxlabel("sample"); fig.supylabel("value")

    elif kind == "polar_profile":
        theta = np.linspace(0, 2 * np.pi, 240)
        r = 1 + 0.28 * np.cos((2 + seed % 4) * theta) + 0.12 * np.sin(5 * theta + seed)
        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        ax.plot(theta, r, color=cycle(seed))
        ax.fill(theta, r, color=cycle(seed), alpha=0.12)
        ax.set_rticks([0.8, 1.0, 1.2, 1.4])

    elif kind == "phase_plane":
        x = np.linspace(-2.4, 2.4, 28)
        y = np.linspace(-2.0, 2.0, 24)
        X, Y = np.meshgrid(x, y)
        U = Y
        V = -0.6 * X - 0.2 * Y + 0.08 * np.sin(seed + X * Y)
        fig, ax = plt.subplots()
        ax.streamplot(X, Y, U, V, color=np.hypot(U, V), cmap=sequential("purple"), density=1.0)
        ax.set_xlabel("state x1"); ax.set_ylabel("state x2")

    elif kind == "distribution":
        rng = _rng(seed)
        a = rng.normal(0, 1, 600)
        b = rng.normal(0.45, 0.75, 600)
        fig, ax = plt.subplots()
        ax.hist(a, bins=32, density=True, alpha=0.45, color=cycle(0), label="baseline")
        ax.hist(b, bins=32, density=True, alpha=0.45, color=cycle(1), label=topic)
        ax.axvline(np.mean(b), color=cycle(1), lw=1.5)
        ax.set_xlabel("value"); ax.set_ylabel("density"); ax.legend()

    elif kind == "bubble_matrix":
        rng = _rng(seed)
        m, n = 7, 7
        X, Y = np.meshgrid(np.arange(n), np.arange(m))
        val = rng.uniform(-1, 1, size=(m, n))
        fig, ax = plt.subplots()
        sc = ax.scatter(X.ravel(), Y.ravel(), s=60 + 420 * np.abs(val.ravel()),
                        c=val.ravel(), cmap=diverging(), vmin=-1, vmax=1, alpha=0.85)
        fig.colorbar(sc, ax=ax, shrink=0.82)
        ax.set_xticks(range(n), _labels("C", n)); ax.set_yticks(range(m), _labels("R", m))

    elif kind == "lollipop":
        rng = _rng(seed)
        vals = np.sort(rng.uniform(0.2, 1.0, 9))
        fig, ax = plt.subplots()
        ax.hlines(np.arange(vals.size), 0, vals, color="0.70")
        ax.scatter(vals, np.arange(vals.size), s=50, color=[cycle(i) for i in range(vals.size)])
        ax.set_yticks(np.arange(vals.size), _labels("factor", vals.size))
        ax.set_xlabel("importance")

    elif kind == "interval_forest":
        rng = _rng(seed)
        mid = rng.normal(0, 0.5, 9)
        lo = mid - rng.uniform(0.15, 0.55, 9)
        hi = mid + rng.uniform(0.15, 0.55, 9)
        y = np.arange(9)
        fig, ax = plt.subplots()
        ax.errorbar(mid, y, xerr=[mid - lo, hi - mid], fmt="o", color=cycle(seed), capsize=3)
        ax.axvline(0, color="0.35", lw=0.8, ls="--")
        ax.set_yticks(y, _labels("study", 9)); ax.set_xlabel("effect")

    elif kind == "stacked_area":
        x = np.arange(80)
        rng = _rng(seed)
        y = rng.gamma(2.0, 0.35, size=(4, x.size))
        y = np.cumsum(y, axis=1)
        y = y / y.max(axis=1, keepdims=True)
        fig, ax = plt.subplots()
        ax.stackplot(x, y, colors=[cycle(i) for i in range(4)], labels=_labels("part", 4), alpha=0.82)
        ax.set_xlabel("sample"); ax.set_ylabel("share"); ax.legend(ncol=4, loc="upper left")

    elif kind == "step_curve":
        rng = _rng(seed)
        x = np.arange(16)
        y = np.cumsum(rng.integers(-2, 5, size=x.size))
        fig, ax = plt.subplots()
        ax.step(x, y, where="post", color=cycle(seed), lw=1.8)
        ax.scatter(x, y, s=22, color=cycle(seed + 1))
        ax.set_xlabel("stage"); ax.set_ylabel("state")

    elif kind == "surface3d":
        x = np.linspace(-2.6, 2.6, 54)
        y = np.linspace(-2.6, 2.6, 54)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X * (1 + (seed % 4) * 0.15)) * np.cos(Y) * np.exp(-0.08 * (X**2 + Y**2))
        fig = plt.figure(figsize=(6.4, 4.6))
        ax = fig.add_subplot(111, projection="3d")
        ax.plot_surface(X, Y, Z, cmap=sequential("green"), linewidth=0, antialiased=True)
        ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("response")

    elif kind == "calendar_grid":
        rng = _rng(seed)
        data = rng.normal(0, 1, (7, 18)) + np.linspace(-0.8, 0.8, 18)
        fig, ax = plt.subplots(figsize=(7.0, 3.5))
        im = ax.imshow(data, aspect="auto", cmap=diverging(), vmin=-2.5, vmax=2.5)
        fig.colorbar(im, ax=ax, shrink=0.78)
        ax.set_yticks(range(7), ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        ax.set_xlabel("week")

    elif kind == "slope":
        rng = _rng(seed)
        a = rng.uniform(0.2, 0.9, 8)
        b = a + rng.normal(0.05, 0.22, 8)
        fig, ax = plt.subplots()
        for i, (v1, v2) in enumerate(zip(a, b)):
            ax.plot([0, 1], [v1, v2], marker="o", color=cycle(i), alpha=0.9)
        ax.set_xticks([0, 1], ["before", "after"]); ax.set_ylabel("metric")

    elif kind == "decision_map":
        rng = _rng(seed)
        x = np.linspace(-3, 3, 160)
        y = np.linspace(-3, 3, 130)
        X, Y = np.meshgrid(x, y)
        Z = np.tanh(0.8 * X - 0.4 * Y + 0.35 * np.sin(seed + X * Y))
        pts = rng.normal(size=(140, 2))
        fig, ax = plt.subplots()
        ax.contourf(X, Y, Z, levels=15, cmap=diverging(), alpha=0.75)
        ax.scatter(pts[:, 0], pts[:, 1], c=(pts[:, 0] - pts[:, 1] > 0), cmap=diverging(), s=16, edgecolor="none")
        ax.set_xlabel("feature 1"); ax.set_ylabel("feature 2")

    else:
        raise ValueError(f"unknown generated pattern kind: {kind}")

    fig.suptitle(f"{domain}: {topic}" if title is None else title, fontsize=10)
    try:
        fig.tight_layout()
    except Exception:
        pass
    return fig
