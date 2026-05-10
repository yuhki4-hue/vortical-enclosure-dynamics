"""Simulate an emergent dynamic barrier from rotational feedback."""

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


BASE_PARAMS = {
    "a": 2.0,
    "b": 1.0,
    "c": 1.0,
    "d": 0.55,
    "e": 0.8,
}
INITIAL_STATE = [-4.0, 0.0, 0.0]
T_SPAN = (0.0, 25.0)
T_EVAL = np.linspace(*T_SPAN, 1200)
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "figures"


def closure_degree(q):
    """Map the unconstrained closure coordinate q into 0 < L < 1."""
    return 1.0 / (1.0 + np.exp(-q))


def dynamic_barrier_system(_t, y, params):
    """ODE system with resistance emerging from rotational feedback only."""
    q, v, omega = y
    a, b, c, d, e = params
    l_value = closure_degree(q)

    dq_dt = v
    # No explicit kappa_B barrier is inserted here.
    # The apparent barrier arises from rotational energy, proportional to omega^2.
    dv_dt = a * l_value - b * omega**2 * l_value - d * v
    domega_dt = c * l_value * v - e * omega

    return [dq_dt, dv_dt, domega_dt]


def parameter_tuple(params):
    """Convert named model parameters to the tuple expected by solve_ivp."""
    return (params["a"], params["b"], params["c"], params["d"], params["e"])


def run_simulation(params):
    """Integrate the dynamic barrier model for a selected parameter set."""
    solution = solve_ivp(
        dynamic_barrier_system,
        T_SPAN,
        INITIAL_STATE,
        args=(parameter_tuple(params),),
        t_eval=T_EVAL,
        rtol=1e-8,
        atol=1e-10,
    )

    if not solution.success:
        raise RuntimeError(f"ODE integration failed: {solution.message}")

    return solution


def save_primary_simulation():
    """Save the baseline simulation of closure, velocity, and rotation."""
    params = dict(BASE_PARAMS)
    solution = run_simulation(params)
    q_values, v_values, omega_values = solution.y
    l_values = closure_degree(q_values)

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(solution.t, l_values, label=r"Closure degree $L(t)$", linewidth=2.2)
    ax.plot(solution.t, v_values, label=r"Closure velocity $v(t)$", linewidth=1.8)
    ax.plot(solution.t, omega_values, label=r"Rotational feedback $\Omega(t)$", linewidth=1.8)

    ax.set_title("Emergent Dynamic Barrier from Rotational Feedback")
    ax.set_xlabel("Time")
    ax.set_ylabel("State variables")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()

    output_path = OUTPUT_DIR / "fig_barrier_01_emergent_barrier.png"
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def save_b_scan():
    """Compare closure for several feedback-resistance strengths B."""
    b_values = [0.0, 0.5, 1.0, 2.0]

    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    for b_value in b_values:
        params = dict(BASE_PARAMS, b=b_value, c=1.2)
        solution = run_simulation(params)
        l_values = closure_degree(solution.y[0])
        ax.plot(solution.t, l_values, label=rf"$B={b_value}$", linewidth=2.0)

    ax.set_title(r"Closure Response for Different $B$ Values")
    ax.set_xlabel("Time")
    ax.set_ylabel(r"Closure degree $L(t)$")
    ax.set_ylim(0.0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(title="Feedback strength", loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_B_scan.png", dpi=300)
    plt.close(fig)


def save_c_scan():
    """Compare closure and rotational feedback for several generation rates C."""
    c_values = [0.2, 0.6, 1.0, 1.5]

    fig, (closure_ax, omega_ax) = plt.subplots(
        2,
        1,
        figsize=(8.0, 6.4),
        sharex=True,
    )

    for c_value in c_values:
        params = dict(BASE_PARAMS, b=1.6, c=c_value)
        solution = run_simulation(params)
        l_values = closure_degree(solution.y[0])
        omega_values = solution.y[2]
        closure_ax.plot(solution.t, l_values, label=rf"$C={c_value}$", linewidth=2.0)
        omega_ax.plot(solution.t, omega_values, label=rf"$C={c_value}$", linewidth=2.0)

    closure_ax.set_title(r"Closure and Rotational Feedback for Different $C$ Values")
    closure_ax.set_ylabel(r"Closure degree $L(t)$")
    closure_ax.set_ylim(0.0, 1.05)
    closure_ax.grid(True, alpha=0.3)
    closure_ax.legend(title="Rotation generation", loc="best")

    omega_ax.set_xlabel("Time")
    omega_ax.set_ylabel(r"Rotational feedback $\Omega(t)$")
    omega_ax.grid(True, alpha=0.3)
    omega_ax.legend(title="Rotation generation", loc="best")

    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_C_scan.png", dpi=300)
    plt.close(fig)


def save_phase_portrait():
    """Plot the quasi-closure attractor approached in the L-Omega plane."""
    params = dict(BASE_PARAMS, b=1.6, c=1.2)
    solution = run_simulation(params)
    l_values = closure_degree(solution.y[0])
    omega_values = solution.y[2]

    fig, ax = plt.subplots(figsize=(6.4, 5.6))
    ax.plot(l_values, omega_values, color="tab:purple", linewidth=2.2)
    ax.scatter(
        l_values[-1],
        omega_values[-1],
        color="black",
        s=55,
        zorder=3,
        label="Quasi-closure attractor",
    )

    ax.set_title(r"Dynamic Barrier Phase Portrait")
    ax.set_xlabel(r"Closure degree $L(t)$")
    ax.set_ylabel(r"Rotational feedback $\Omega(t)$")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "dynamic_barrier_phase_portrait.png", dpi=300)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    save_primary_simulation()
    save_b_scan()
    save_c_scan()
    save_phase_portrait()


if __name__ == "__main__":
    main()
