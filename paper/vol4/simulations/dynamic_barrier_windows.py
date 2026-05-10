"""Observation-window diagnostics for the dynamic barrier model.

These diagnostics do not introduce new physical variables.  They are
different observation windows on the same closure--rotation--dissipation
ODE system, used to show how apparent rest in one projection can reappear
as motion in another.
"""

import os
import tempfile
from pathlib import Path

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "ved_dynamic_barrier_windows_mpl"),
)
os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(tempfile.gettempdir()) / "ved_dynamic_barrier_windows_cache"),
)

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks, welch


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "figures"

INITIAL_STATE = (-4.0, 0.0, 0.0)

PRESETS = {
    "baseline": {"A": 2.0, "B": 1.0, "C": 1.0, "D": 0.55, "E": 0.8},
    "conservative_rotation": {"A": 1.0, "B": 1.0, "C": 1.0, "D": None, "E": 0.0},
    "window_test": {
        "A": 1.0,
        "B": 1.0,
        "C": 1.0,
        "D_values": [0.005, 0.02, 0.10],
        "E": 0.0,
    },
}


def closure_degree(q):
    """Sigmoid closure degree, clipped only to avoid numerical overflow."""
    return 1.0 / (1.0 + np.exp(-np.clip(q, -60.0, 60.0)))


def rhs(_t, y, params):
    """Dynamic barrier ODE with no explicit kappa_B potential term."""
    q, v, omega = y
    L = closure_degree(q)
    A, B, C, D, E = (params[key] for key in ("A", "B", "C", "D", "E"))

    dq_dt = v
    dv_dt = A * L - B * omega**2 * L - D * v
    domega_dt = C * L * v - E * omega
    return (dq_dt, dv_dt, domega_dt)


def integrate(params, t_end=300.0, samples=9000):
    """Integrate the shared model for a chosen observation window."""
    t_eval = np.linspace(0.0, t_end, samples)
    solution = solve_ivp(
        rhs,
        (0.0, t_end),
        INITIAL_STATE,
        args=(params,),
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-11,
    )
    if not solution.success:
        raise RuntimeError(f"ODE integration failed: {solution.message}")
    return solution


def conservative_params(D):
    """Preset for the E=0 conservative-rotation observation tests."""
    params = dict(PRESETS["conservative_rotation"])
    params["D"] = D
    return params


def centered_omega(omega, params):
    """Center Omega around the late closure balance sqrt(A/B)."""
    return omega - np.sqrt(params["A"] / params["B"])


def late_slice(t, fraction=0.65):
    """Return a slice selecting the late part of a trajectory."""
    start = int((1.0 - fraction) * len(t))
    return slice(start, None)


def mark_spectral_peaks(ax, frequencies, power, min_frequency=0.01):
    """Annotate the strongest few spectral peaks for readability."""
    valid = frequencies > min_frequency
    if not np.any(valid):
        return
    peak_indices, _ = find_peaks(power[valid])
    valid_indices = np.flatnonzero(valid)
    if len(peak_indices) == 0:
        return

    absolute_peaks = valid_indices[peak_indices]
    strongest = absolute_peaks[np.argsort(power[absolute_peaks])[-4:]]
    for index in strongest:
        ax.axvline(frequencies[index], color="black", alpha=0.18, linewidth=0.9)


def save_phase_spiral():
    """Plot E=0 phase rotation in the centered (v, Omega) plane."""
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    colors = ["tab:blue", "tab:orange", "tab:green"]

    for color, D in zip(colors, PRESETS["window_test"]["D_values"]):
        params = conservative_params(D)
        solution = integrate(params)
        v = solution.y[1]
        omega_c = centered_omega(solution.y[2], params)
        tail = late_slice(solution.t, fraction=0.78)
        ax.plot(v[tail], omega_c[tail], color=color, linewidth=1.4, label=rf"$D={D:g}$")
        ax.scatter(v[-1], omega_c[-1], color=color, s=24, zorder=3)

    ax.axhline(0.0, color="black", linewidth=0.8, alpha=0.35)
    ax.axvline(0.0, color="black", linewidth=0.8, alpha=0.35)
    ax.set_title("Phase Rotation Around the Closure Balance")
    ax.set_xlabel(r"$v$")
    ax.set_ylabel(r"$\Omega-\sqrt{A/B}$")
    ax.grid(True, alpha=0.28)
    ax.legend(title="Velocity dissipation", loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_01_phase_spiral.pdf")
    plt.close(fig)


def sliding_extent(v, omega_c, t, window_time=16.0, stride_time=2.0):
    """Compute the phase-space extent inside sliding time windows."""
    dt = float(np.mean(np.diff(t)))
    window = max(8, int(window_time / dt))
    stride = max(1, int(stride_time / dt))
    centers = []
    extents = []

    for start in range(0, len(t) - window, stride):
        stop = start + window
        points = np.column_stack((v[start:stop], omega_c[start:stop]))
        center = np.mean(points, axis=0)
        radius = np.linalg.norm(points - center, axis=1)
        extent = max(np.max(radius), 1e-14)
        centers.append(0.5 * (t[start] + t[stop - 1]))
        extents.append(extent)

    return np.asarray(centers), np.asarray(extents)


def save_extent_decay():
    """Show that a finite-window orbit extent decays approximately exponentially."""
    fig, ax = plt.subplots(figsize=(7.0, 4.8))

    for D in PRESETS["window_test"]["D_values"]:
        params = conservative_params(D)
        solution = integrate(params)
        v = solution.y[1]
        omega_c = centered_omega(solution.y[2], params)
        centers, extents = sliding_extent(v, omega_c, solution.t)
        late = centers > 60.0
        ax.plot(centers[late], np.log(extents[late]), linewidth=1.9, label=rf"$D={D:g}$")

    ax.set_title("Finite-Window Phase Extent Decay")
    ax.set_xlabel("Window center time")
    ax.set_ylabel(r"$\log(\mathrm{extent})$")
    ax.grid(True, alpha=0.28)
    ax.legend(title="Velocity dissipation", loc="best")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_02_extent_decay.pdf")
    plt.close(fig)


def spectrum_of(signal, t):
    """Welch spectrum of a one-dimensional observation window."""
    dt = float(np.mean(np.diff(t)))
    fs = 1.0 / dt
    nperseg = min(2048, len(signal))
    frequencies, power = welch(
        signal - np.mean(signal),
        fs=fs,
        nperseg=nperseg,
        scaling="density",
    )
    return frequencies, power


def save_spectrum():
    """Plot harmonic content generated by the nonlinear sigmoid feedback."""
    params = conservative_params(0.02)
    solution = integrate(params)
    tail = late_slice(solution.t, fraction=0.75)
    t_tail = solution.t[tail]
    v_tail = solution.y[1][tail]
    frequencies, power = spectrum_of(v_tail, t_tail)

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.semilogy(frequencies, power, color="tab:purple", linewidth=1.9)
    mark_spectral_peaks(ax, frequencies, power)
    ax.set_xlim(0.0, 1.2)
    ax.set_title(r"Spectrum of the Closure Velocity $v(t)$")
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Power spectral density")
    ax.grid(True, alpha=0.28)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_03_spectrum.pdf")
    plt.close(fig)


def save_delay_embedding():
    """Plot a delay embedding of v(t) as an observation-window diagnostic."""
    params = conservative_params(0.02)
    solution = integrate(params)
    tail = late_slice(solution.t, fraction=0.70)
    v = solution.y[1][tail]
    tau = 90
    usable = len(v) - 2 * tau
    x = v[:usable]
    y = v[tau : tau + usable]
    z = v[2 * tau : 2 * tau + usable]

    fig = plt.figure(figsize=(6.8, 5.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(x, y, z, color="tab:blue", linewidth=1.0, alpha=0.92)
    ax.set_title(r"Delay Embedding of $v(t)$")
    ax.set_xlabel(r"$v(t)$")
    ax.set_ylabel(r"$v(t+\tau)$")
    ax.set_zlabel(r"$v(t+2\tau)$")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_04_delay_embedding.pdf")
    plt.close(fig)


def save_high_derivative_space():
    """Plot higher-order phase structure in (v, dv/dt, d2v/dt2)."""
    params = conservative_params(0.02)
    solution = integrate(params)
    q, v, omega = solution.y
    L = closure_degree(q)
    dv_dt = params["A"] * L - params["B"] * omega**2 * L - params["D"] * v
    d2v_dt2 = np.gradient(dv_dt, solution.t)

    tail = late_slice(solution.t, fraction=0.70)
    fig = plt.figure(figsize=(6.8, 5.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(v[tail], dv_dt[tail], d2v_dt2[tail], color="tab:red", linewidth=1.0)
    ax.set_title("Higher-Order Phase Structure")
    ax.set_xlabel(r"$v$")
    ax.set_ylabel(r"$dv/dt$")
    ax.set_zlabel(r"$d^2v/dt^2$")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_05_high_derivative_space.pdf")
    plt.close(fig)


def save_envelope_spectrum():
    """Analyze modulation of the decaying radial envelope."""
    params = conservative_params(0.02)
    solution = integrate(params)
    tail = late_slice(solution.t, fraction=0.80)
    t_tail = solution.t[tail]
    v_tail = solution.y[1][tail]
    omega_c = centered_omega(solution.y[2][tail], params)
    radius = np.sqrt(v_tail**2 + omega_c**2)
    log_radius = np.log(np.maximum(radius, 1e-14))
    finite = np.isfinite(log_radius)
    trend_coefficients = np.polyfit(t_tail[finite], log_radius[finite], deg=1)
    trend = np.polyval(trend_coefficients, t_tail)
    residual = log_radius - trend
    frequencies, power = spectrum_of(residual, t_tail)

    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    ax.semilogy(frequencies, power, color="tab:green", linewidth=1.9)
    mark_spectral_peaks(ax, frequencies, power)
    ax.set_xlim(0.0, 1.2)
    ax.set_title("Spectrum of the Detrended Envelope")
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Power spectral density")
    ax.grid(True, alpha=0.28)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "fig_barrier_window_06_envelope_spectrum.pdf")
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    save_phase_spiral()
    save_extent_decay()
    save_spectrum()
    save_delay_embedding()
    save_high_derivative_space()
    save_envelope_spectrum()


if __name__ == "__main__":
    main()
