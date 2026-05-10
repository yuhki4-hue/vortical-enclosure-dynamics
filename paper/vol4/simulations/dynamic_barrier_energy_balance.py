"""Energy-balance diagnostics for the emergent dynamic barrier model."""

import csv

import numpy as np

from dynamic_barrier_model import BASE_PARAMS, OUTPUT_DIR, closure_degree, run_simulation

import matplotlib.pyplot as plt


CSV_PATH = OUTPUT_DIR.parent / "simulations" / "dynamic_barrier_energy_balance.csv"


def cumulative_integral(values, times):
    """Compute cumulative trapezoidal integral without adding new dependencies."""
    increments = 0.5 * (values[1:] + values[:-1]) * np.diff(times)
    return np.concatenate(([0.0], np.cumsum(increments)))


def compute_energy_balance():
    """Compute energy and power diagnostics for the baseline trajectory."""
    params = dict(BASE_PARAMS)
    solution = run_simulation(params)

    t_values = solution.t
    q_values, v_values, omega_values = solution.y
    l_values = closure_degree(q_values)

    a_value = params["a"]
    b_value = params["b"]
    d_value = params["d"]
    e_value = params["e"]

    e_v = 0.5 * v_values**2
    e_omega = 0.5 * omega_values**2

    # P_drive injects closure motion.
    p_drive = a_value * l_values * v_values
    # P_feedback converts rotational feedback into anti-closure resistance.
    p_feedback = b_value * omega_values**2 * l_values * v_values
    # P_D and P_Omega remove excess motion and allow stable quasi-closure.
    p_d = d_value * v_values**2
    p_omega = e_value * omega_values**2

    cumulative_drive = cumulative_integral(p_drive, t_values)
    cumulative_feedback = cumulative_integral(p_feedback, t_values)
    cumulative_dissipation = cumulative_integral(p_d + p_omega, t_values)

    return {
        "t": t_values,
        "L": l_values,
        "v": v_values,
        "Omega": omega_values,
        "E_v": e_v,
        "E_Omega": e_omega,
        "P_drive": p_drive,
        "P_feedback": p_feedback,
        "P_D": p_d,
        "P_Omega": p_omega,
        "cumulative_drive": cumulative_drive,
        "cumulative_feedback": cumulative_feedback,
        "cumulative_dissipation": cumulative_dissipation,
    }


def save_energy_states(data):
    """Plot closure, closure kinetic energy, and rotational feedback energy."""
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(data["t"], data["L"], label=r"Closure degree $L(t)$", linewidth=2.2)
    ax.plot(data["t"], data["E_v"], label=r"Closure kinetic energy $E_v$", linewidth=1.9)
    # E_Omega stores rotational feedback energy.
    ax.plot(data["t"], data["E_Omega"], label=r"Rotational energy $E_\Omega$", linewidth=1.9)

    ax.set_title("Dynamic Barrier Energy States")
    ax.set_xlabel("Time")
    ax.set_ylabel("State / energy")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_04_energy_states.png", dpi=300)
    plt.close(fig)


def save_power_balance(data):
    """Plot closure drive, feedback resistance, and dissipation powers."""
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(data["t"], data["P_drive"], label=r"$P_{\mathrm{drive}}$", linewidth=2.0)
    ax.plot(data["t"], data["P_feedback"], label=r"$P_{\mathrm{feedback}}$", linewidth=2.0)
    ax.plot(data["t"], data["P_D"], label=r"$P_D$", linewidth=2.0)
    ax.plot(data["t"], data["P_Omega"], label=r"$P_\Omega$", linewidth=2.0)

    ax.set_title("Dynamic Barrier Power Balance")
    ax.set_xlabel("Time")
    ax.set_ylabel("Power")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_05_power_balance.png", dpi=300)
    plt.close(fig)


def save_cumulative_energy(data):
    """Plot cumulative injected, resisted, and dissipated energy."""
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(
        data["t"],
        data["cumulative_drive"],
        label=r"$\int P_{\mathrm{drive}}\,dt$",
        linewidth=2.1,
    )
    ax.plot(
        data["t"],
        data["cumulative_feedback"],
        label=r"$\int P_{\mathrm{feedback}}\,dt$",
        linewidth=2.1,
    )
    ax.plot(
        data["t"],
        data["cumulative_dissipation"],
        label=r"$\int (P_D + P_\Omega)\,dt$",
        linewidth=2.1,
    )

    ax.set_title("Dynamic Barrier Cumulative Energy Balance")
    ax.set_xlabel("Time")
    ax.set_ylabel("Cumulative energy")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_06_cumulative_energy.png", dpi=300)
    plt.close(fig)


def save_csv(data):
    """Save time-resolved energy-balance diagnostics."""
    columns = [
        "t",
        "L",
        "v",
        "Omega",
        "E_v",
        "E_Omega",
        "P_drive",
        "P_feedback",
        "P_D",
        "P_Omega",
        "cumulative_drive",
        "cumulative_feedback",
        "cumulative_dissipation",
    ]

    with CSV_PATH.open("w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        for index in range(len(data["t"])):
            writer.writerow([data[column][index] for column in columns])


def main():
    # Without dissipation, the system remains oscillatory rather than forming
    # a stable quasi-closure structure.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = compute_energy_balance()
    save_energy_states(data)
    save_power_balance(data)
    save_cumulative_energy(data)
    save_csv(data)


if __name__ == "__main__":
    main()
