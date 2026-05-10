"""Map dynamic barrier regimes across velocity dissipation D and feedback B."""

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
from matplotlib.colors import BoundaryNorm, ListedColormap
from matplotlib.patches import Patch
from scipy.integrate import solve_ivp


A = 1.0
C = 1.0
E = 0.4
INITIAL_STATE = [-4.0, 0.0, 0.0]
T_SPAN = (0.0, 60.0)
T_EVAL = np.linspace(*T_SPAN, 1500)
D_VALUES = np.linspace(0.0, 0.8, 41)
B_VALUES = np.linspace(0.0, 3.0, 41)

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"
CSV_PATH = SCRIPT_DIR / "dynamic_barrier_phase_diagram_DB.csv"

REGIME_LABELS = {
    0: "overdamped_or_delayed",
    1: "stable_quasi_closure",
    2: "near_complete_closure",
    3: "limit_cycle_like",
}


def closure_degree(q):
    """Map the unconstrained closure coordinate q into 0 < L < 1."""
    return 1.0 / (1.0 + np.exp(-q))


def dynamic_barrier_system(_t, y, params):
    """ODE with no explicit kappa_B barrier term."""
    b_value, d_value = params
    q, v, omega = y
    l_value = closure_degree(q)

    dq_dt = v
    # This scan tests whether stable quasi-closure requires both rotational
    # feedback (B) and direct velocity dissipation (D).
    dv_dt = A * l_value - b_value * omega**2 * l_value - d_value * v
    domega_dt = C * l_value * v - E * omega

    return [dq_dt, dv_dt, domega_dt]


def classify_trajectory(solution):
    """Classify the late-time regime from the final quarter of the trajectory."""
    q_values, v_values, omega_values = solution.y
    l_values = closure_degree(q_values)
    tail_start = int(0.75 * len(solution.t))

    v_tail = v_values[tail_start:]
    omega_tail = omega_values[tail_start:]
    std_v_tail = float(np.std(v_tail))
    std_omega_tail = float(np.std(omega_tail))
    final_l = float(l_values[-1])

    if final_l < 0.8:
        regime = 0
    elif std_v_tail > 0.05 or std_omega_tail > 0.05:
        regime = 3
    elif final_l >= 0.995:
        regime = 2
    else:
        regime = 1

    return final_l, std_v_tail, std_omega_tail, regime


def run_scan():
    """Integrate the model for all points in the D-B parameter plane."""
    regime_grid = np.zeros((len(B_VALUES), len(D_VALUES)), dtype=int)
    rows = []

    for b_index, b_value in enumerate(B_VALUES):
        for d_index, d_value in enumerate(D_VALUES):
            solution = solve_ivp(
                dynamic_barrier_system,
                T_SPAN,
                INITIAL_STATE,
                args=((b_value, d_value),),
                t_eval=T_EVAL,
                rtol=1e-7,
                atol=1e-9,
            )
            if not solution.success:
                raise RuntimeError(
                    f"Integration failed for D={d_value:.3f}, B={b_value:.3f}: "
                    f"{solution.message}"
                )

            final_l, std_v_tail, std_omega_tail, regime = classify_trajectory(solution)
            regime_grid[b_index, d_index] = regime
            rows.append(
                {
                    "D": d_value,
                    "B": b_value,
                    "final_L": final_l,
                    "std_v_tail": std_v_tail,
                    "std_Omega_tail": std_omega_tail,
                    "regime_label": REGIME_LABELS[regime],
                }
            )

    return regime_grid, rows


def save_csv(rows):
    """Write phase-diagram diagnostics for later inspection."""
    with CSV_PATH.open("w", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "D",
                "B",
                "final_L",
                "std_v_tail",
                "std_Omega_tail",
                "regime_label",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def save_heatmap(regime_grid):
    """Save the D-B qualitative-regime phase diagram."""
    colors = ["#7f8c8d", "#2ca25f", "#fdae61", "#6a51a3"]
    display_labels = [
        "over-damped / delayed",
        "stable quasi-closure",
        "near-complete closure",
        "limit-cycle-like",
    ]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap.N)

    fig, ax = plt.subplots(figsize=(8.2, 6.4))
    image = ax.imshow(
        regime_grid,
        origin="lower",
        aspect="auto",
        cmap=cmap,
        norm=norm,
        extent=[D_VALUES.min(), D_VALUES.max(), B_VALUES.min(), B_VALUES.max()],
    )

    ax.set_title(r"Dynamic Barrier Phase Diagram in $(D, B)$")
    ax.set_xlabel(r"Velocity dissipation $D$")
    ax.set_ylabel(r"Rotational feedback strength $B$")

    handles = [
        Patch(facecolor=colors[index], edgecolor="black", label=label)
        for index, label in enumerate(display_labels)
    ]
    ax.legend(handles=handles, loc="upper right", frameon=True)

    colorbar = fig.colorbar(image, ax=ax, ticks=[0, 1, 2, 3], pad=0.03)
    colorbar.ax.set_yticklabels(display_labels)
    colorbar.set_label("Late-time regime")

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_03_phase_diagram_DB.png", dpi=300)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    regime_grid, rows = run_scan()
    save_csv(rows)
    save_heatmap(regime_grid)


if __name__ == "__main__":
    main()
