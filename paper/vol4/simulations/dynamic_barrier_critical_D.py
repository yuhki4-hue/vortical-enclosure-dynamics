"""Critical-limit analysis of the dynamic barrier model as D approaches zero."""

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
from scipy.integrate import solve_ivp


A = 1.0
B = 1.0
C = 1.0
E = 0.4
INITIAL_STATE = [-4.0, 0.0, 0.0]
T_SPAN = (0.0, 120.0)
T_EVAL = np.linspace(*T_SPAN, 2400)
D_VALUES = np.unique(
    np.concatenate(
        [
            np.linspace(0.0, 0.02, 11),
            np.linspace(0.025, 0.2, 15),
            np.linspace(0.25, 0.8, 12),
        ]
    )
)

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"
CSV_PATH = SCRIPT_DIR / "dynamic_barrier_critical_D.csv"


def closure_degree(q):
    """Map the unconstrained closure coordinate q into 0 < L < 1."""
    return 1.0 / (1.0 + np.exp(-q))


def dynamic_barrier_system(_t, y, d_value):
    """ODE with rotational feedback but no explicit barrier potential."""
    q, v, omega = y
    l_value = closure_degree(q)

    dq_dt = v
    # D -> 0 tests the disappearance of dissipative stabilization.
    # Rotational feedback prevents immediate closure, but cannot by itself
    # create a stable quasi-closure structure.
    dv_dt = A * l_value - B * omega**2 * l_value - d_value * v
    domega_dt = C * l_value * v - E * omega

    return [dq_dt, dv_dt, domega_dt]


def integrate_for_d(d_value):
    """Integrate the model for one velocity dissipation value."""
    solution = solve_ivp(
        dynamic_barrier_system,
        T_SPAN,
        INITIAL_STATE,
        args=(d_value,),
        t_eval=T_EVAL,
        rtol=1e-7,
        atol=1e-9,
    )
    if not solution.success:
        raise RuntimeError(f"Integration failed for D={d_value:.6f}: {solution.message}")

    return solution


def diagnose_solution(d_value, solution):
    """Compute final-tail diagnostics for one trajectory."""
    q_values, v_values, omega_values = solution.y
    l_values = closure_degree(q_values)
    tail_start = int(0.7 * len(solution.t))

    l_tail = l_values[tail_start:]
    v_tail = v_values[tail_start:]
    omega_tail = omega_values[tail_start:]
    std_v_tail = float(np.std(v_tail))
    std_omega_tail = float(np.std(omega_tail))

    return {
        "D": float(d_value),
        "final_L": float(l_values[-1]),
        "mean_L_tail": float(np.mean(l_tail)),
        "std_L_tail": float(np.std(l_tail)),
        "mean_v_tail": float(np.mean(v_tail)),
        "std_v_tail": std_v_tail,
        "mean_Omega_tail": float(np.mean(omega_tail)),
        "std_Omega_tail": std_omega_tail,
        "oscillation_amplitude_v": float(np.max(v_tail) - np.min(v_tail)),
        "oscillation_amplitude_Omega": float(np.max(omega_tail) - np.min(omega_tail)),
        "instability_indicator": std_v_tail + std_omega_tail,
    }


def run_scan():
    """Scan small D values to find where stable quasi-closure appears."""
    rows = []
    for d_value in D_VALUES:
        solution = integrate_for_d(d_value)
        rows.append(diagnose_solution(d_value, solution))

    return rows


def estimate_critical_d(rows):
    """Return the smallest D with I(D) < 0.05, if present."""
    for row in sorted(rows, key=lambda item: item["D"]):
        if row["instability_indicator"] < 0.05:
            return row["D"]

    return None


def save_csv(rows):
    """Save critical-D diagnostics."""
    columns = [
        "D",
        "final_L",
        "mean_L_tail",
        "std_L_tail",
        "mean_v_tail",
        "std_v_tail",
        "mean_Omega_tail",
        "std_Omega_tail",
        "oscillation_amplitude_v",
        "oscillation_amplitude_Omega",
        "instability_indicator",
    ]

    with CSV_PATH.open("w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def save_instability_plot(rows, critical_d):
    """Plot I(D) = std(v_tail) + std(Omega_tail)."""
    d_values = np.array([row["D"] for row in rows])
    instability = np.array([row["instability_indicator"] for row in rows])

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(d_values, instability, marker="o", linewidth=2.0, markersize=4)
    ax.axhline(0.05, color="black", linestyle="--", linewidth=1.4, label=r"$I(D)=0.05$")
    if critical_d is not None:
        ax.axvline(
            critical_d,
            color="tab:red",
            linestyle=":",
            linewidth=1.8,
            label=rf"$D_c={critical_d:.4f}$",
        )

    ax.set_title(r"Critical Dissipation Threshold for Quasi-Closure")
    ax.set_xlabel(r"Velocity dissipation $D$")
    ax.set_ylabel(r"Instability indicator $I(D)$")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_critical_D_instability.png", dpi=300)
    plt.close(fig)


def save_amplitude_plot(rows):
    """Plot late-time oscillation amplitudes against D."""
    d_values = np.array([row["D"] for row in rows])
    amplitude_v = np.array([row["oscillation_amplitude_v"] for row in rows])
    amplitude_omega = np.array([row["oscillation_amplitude_Omega"] for row in rows])

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(d_values, amplitude_v, marker="o", label=r"$\Delta v_{\mathrm{tail}}$", linewidth=2.0)
    ax.plot(
        d_values,
        amplitude_omega,
        marker="s",
        label=r"$\Delta \Omega_{\mathrm{tail}}$",
        linewidth=2.0,
    )

    ax.set_title(r"Late-Time Oscillation Amplitude as $D \to 0$")
    ax.set_xlabel(r"Velocity dissipation $D$")
    ax.set_ylabel("Oscillation amplitude")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_critical_D_amplitude.png", dpi=300)
    plt.close(fig)


def save_closure_plot(rows):
    """Plot mean closure and closure fluctuation in the final tail."""
    d_values = np.array([row["D"] for row in rows])
    mean_l = np.array([row["mean_L_tail"] for row in rows])
    std_l = np.array([row["std_L_tail"] for row in rows])

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(d_values, mean_l, marker="o", label=r"$\langle L\rangle_{\mathrm{tail}}$", linewidth=2.0)
    ax.plot(d_values, std_l, marker="s", label=r"$\sigma(L)_{\mathrm{tail}}$", linewidth=2.0)

    ax.set_title(r"Closure Statistics Near the Critical Dissipation Limit")
    ax.set_xlabel(r"Velocity dissipation $D$")
    ax.set_ylabel("Closure statistic")
    ax.set_ylim(bottom=0.0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_critical_D_closure.png", dpi=300)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = run_scan()
    critical_d = estimate_critical_d(rows)

    save_csv(rows)
    save_instability_plot(rows, critical_d)
    save_amplitude_plot(rows)
    save_closure_plot(rows)

    # Stable quasi-closure appears only above a finite dissipation threshold.
    if critical_d is None:
        print("D_c: no threshold found")
    else:
        print(f"D_c: {critical_d:.6f}")


if __name__ == "__main__":
    main()
