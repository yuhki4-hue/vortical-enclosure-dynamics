"""Test closure stabilization when direct velocity dissipation is varied."""

from dynamic_barrier_model import BASE_PARAMS, OUTPUT_DIR, closure_degree, run_simulation

import matplotlib.pyplot as plt


D_VALUES = [0.0, 0.05, 0.1, 0.2, 0.5]


def run_d_scan():
    """Run the baseline dynamic barrier model for several D values."""
    results = {}
    for d_value in D_VALUES:
        # D controls direct dissipation of closure velocity.
        # D=0 tests whether rotational feedback alone can prevent complete closure.
        params = dict(BASE_PARAMS, d=d_value)
        solution = run_simulation(params)
        results[d_value] = {
            "t": solution.t,
            "L": closure_degree(solution.y[0]),
            "v": solution.y[1],
            "Omega": solution.y[2],
        }

    return results


def save_time_scan(results, variable, ylabel, filename):
    """Save a time-series comparison for one state variable."""
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    for d_value, data in results.items():
        ax.plot(data["t"], data[variable], label=rf"$D={d_value}$", linewidth=2.0)

    ax.set_title(rf"Dissipation Scan: ${ylabel}$")
    ax.set_xlabel("Time")
    ax.set_ylabel(rf"${ylabel}$")
    if variable == "L":
        ax.set_ylim(0.0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(title="Velocity dissipation", loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.close(fig)


def save_phase_scan(results, x_key, y_key, xlabel, ylabel, filename):
    """Save phase portraits for each D value."""
    fig, ax = plt.subplots(figsize=(6.4, 5.6))
    for d_value, data in results.items():
        ax.plot(data[x_key], data[y_key], label=rf"$D={d_value}$", linewidth=1.9)
        ax.scatter(data[x_key][-1], data[y_key][-1], s=25, zorder=3)

    ax.set_title(rf"Dissipation Phase Scan: ${xlabel}$ vs. ${ylabel}$")
    ax.set_xlabel(rf"${xlabel}$")
    ax.set_ylabel(rf"${ylabel}$")
    ax.grid(True, alpha=0.3)
    ax.legend(title="Velocity dissipation", loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = run_d_scan()

    save_time_scan(results, "L", "L(t)", "dynamic_barrier_D_scan_L.png")
    save_time_scan(results, "v", "v(t)", "dynamic_barrier_D_scan_v.png")
    save_time_scan(results, "Omega", r"\Omega(t)", "fig_barrier_10_omega_dissipation_scan.png")

    # Oscillations or limit-cycle-like behavior in these portraits would suggest
    # that dissipation is needed for coherent quasi-closure stabilization.
    save_phase_scan(
        results,
        "L",
        "Omega",
        "L(t)",
        r"\Omega(t)",
        "dynamic_barrier_D_scan_phase_LOmega.png",
    )
    save_phase_scan(
        results,
        "L",
        "v",
        "L(t)",
        "v(t)",
        "dynamic_barrier_D_scan_phase_Lv.png",
    )
    save_phase_scan(
        results,
        "v",
        "Omega",
        "v(t)",
        r"\Omega(t)",
        "fig_barrier_02_phase_scan_v_omega.png",
    )


if __name__ == "__main__":
    main()
