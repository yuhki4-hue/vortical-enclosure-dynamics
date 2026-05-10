"""Threshold sensitivity analysis for the critical dissipation D_c.

This script does not re-integrate the ODE. It reads the diagnostics produced by
dynamic_barrier_critical_D_no_rotation_damping.py and recomputes D_c under
different choices of the instability threshold.
"""

import csv
import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "ved_dynamic_barrier_mpl"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "ved_dynamic_barrier_cache"),
)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


THRESHOLDS = [0.01, 0.02, 0.03, 0.05, 0.07, 0.10]

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_CSV = SCRIPT_DIR / "dynamic_barrier_critical_D_no_rotation_damping.csv"
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"
OUTPUT_CSV = SCRIPT_DIR / "dynamic_barrier_Dc_threshold_sensitivity.csv"


def load_instability_data():
    """Load D and I(D) from the existing critical-D scan output."""
    if not INPUT_CSV.exists():
        raise FileNotFoundError(
            f"Required input not found: {INPUT_CSV}. "
            "Run dynamic_barrier_critical_D_no_rotation_damping.py first."
        )

    d_values = []
    instability = []
    with INPUT_CSV.open("r", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            d_values.append(float(row["D"]))
            instability.append(float(row["instability_indicator"]))

    order = np.argsort(d_values)
    return np.array(d_values)[order], np.array(instability)[order]


def estimate_dc(d_values, instability, threshold):
    """Return the smallest D such that I(D) < threshold."""
    for d_value, indicator in zip(d_values, instability):
        if indicator < threshold:
            return float(d_value)
    return None


def save_csv(rows):
    """Write threshold-to-D_c table."""
    with OUTPUT_CSV.open("w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["threshold", "D_c"])
        for threshold, d_c in rows:
            writer.writerow([threshold, "" if d_c is None else f"{d_c:.6f}"])


def save_sensitivity_plot(d_values, instability, rows):
    """Plot I(D) with threshold lines and D_c crossing points."""
    fig, ax = plt.subplots(figsize=(8.6, 5.2))
    ax.plot(
        d_values,
        instability,
        marker="o",
        linewidth=2.0,
        markersize=4,
        color="tab:blue",
        label=r"$I(D)=\sigma(v)_{\mathrm{tail}}+\sigma(\Omega)_{\mathrm{tail}}$",
        zorder=2,
    )

    colormap = plt.get_cmap("viridis")
    for index, (threshold, d_c) in enumerate(rows):
        color = colormap(index / max(1, len(rows) - 1))
        ax.axhline(
            threshold,
            color=color,
            linestyle="--",
            linewidth=1.2,
            alpha=0.7,
        )
        if d_c is not None:
            ax.axvline(
                d_c,
                color=color,
                linestyle=":",
                linewidth=1.2,
                alpha=0.7,
            )
            ax.scatter(
                [d_c],
                [threshold],
                color=color,
                s=55,
                zorder=3,
                label=rf"$\theta={threshold:.2f}\Rightarrow D_c={d_c:.4f}$",
            )

    ax.set_title(r"Threshold Sensitivity of the Critical Dissipation $D_c$")
    ax.set_xlabel(r"Velocity dissipation $D$")
    ax.set_ylabel(r"Instability indicator $I(D)$")
    ax.set_xlim(left=0.0, right=max(0.3, float(d_values.max())))
    ax.set_ylim(bottom=0.0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_11_Dc_threshold_sensitivity.png", dpi=300)
    plt.close(fig)


def save_dc_vs_threshold_plot(rows):
    """Plot D_c as a function of the chosen threshold theta."""
    valid = [(theta, d_c) for theta, d_c in rows if d_c is not None]
    if not valid:
        return

    thetas = np.array([theta for theta, _ in valid])
    dcs = np.array([d_c for _, d_c in valid])

    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.plot(thetas, dcs, marker="o", linewidth=2.0, color="tab:red")

    for theta, d_c in valid:
        ax.annotate(
            f"{d_c:.4f}",
            xy=(theta, d_c),
            xytext=(6, 6),
            textcoords="offset points",
            fontsize=9,
        )

    ax.set_title(r"$D_c$ Estimate vs. Instability Threshold $\theta$")
    ax.set_xlabel(r"Instability threshold $\theta$")
    ax.set_ylabel(r"Estimated $D_c(\theta)$")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_12_Dc_vs_threshold.png", dpi=300)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    d_values, instability = load_instability_data()
    rows = [
        (threshold, estimate_dc(d_values, instability, threshold))
        for threshold in THRESHOLDS
    ]

    save_csv(rows)
    save_sensitivity_plot(d_values, instability, rows)
    save_dc_vs_threshold_plot(rows)

    print("threshold theta -> D_c(theta)")
    for threshold, d_c in rows:
        if d_c is None:
            print(f"  theta = {threshold:.2f}: no crossing in scanned range")
        else:
            print(f"  theta = {threshold:.2f}: D_c = {d_c:.6f}")


if __name__ == "__main__":
    main()
