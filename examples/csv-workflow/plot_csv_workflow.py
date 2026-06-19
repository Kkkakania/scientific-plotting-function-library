#!/usr/bin/env python3
"""Render a clean-room CSV measurement example as a publication-style figure."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_measurements(csv_path: Path) -> dict[str, list[float]]:
    data = {
        "time_s": [],
        "voltage_v": [],
        "current_a": [],
        "temperature_c": [],
    }
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            for key in data:
                data[key].append(float(row[key]))
    return data


def make_figure(data: dict[str, list[float]]) -> plt.Figure:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.4,
    })

    fig, axes = plt.subplots(2, 1, figsize=(3.5, 4.2), sharex=True, constrained_layout=True)
    time_s = data["time_s"]

    axes[0].plot(time_s, data["voltage_v"], marker="o", color="#0072B2", label="Voltage")
    axes[0].set_ylabel("Voltage (V)")
    axes[0].legend(frameon=False, loc="lower right")
    axes[0].grid(True, color="#DDDDDD", linewidth=0.6)
    axes[0].text(0.02, 0.92, "(a)", transform=axes[0].transAxes, fontweight="bold")

    axes[1].plot(time_s, data["current_a"], marker="s", color="#E69F00", label="Current")
    axes[1].set_xlabel("Time (s)")
    axes[1].set_ylabel("Current (A)")
    axes[1].legend(frameon=False, loc="lower right")
    axes[1].grid(True, color="#DDDDDD", linewidth=0.6)
    axes[1].text(0.02, 0.92, "(b)", transform=axes[1].transAxes, fontweight="bold")

    return fig


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path(__file__).with_name("sample_measurements.csv"))
    parser.add_argument("--out-dir", type=Path, default=Path("out"))
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    data = load_measurements(args.csv)
    fig = make_figure(data)

    stem = "csv_workflow_voltage_current"
    fig.savefig(args.out_dir / f"{stem}.png", dpi=300)
    fig.savefig(args.out_dir / f"{stem}.pdf")
    plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
