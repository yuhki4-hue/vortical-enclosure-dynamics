"""Minimal Bio-IFGT neural-field toy simulation.

This is an illustrative 2D model, not a realistic embryogenesis model.
DNA-like influence is represented only by editable parameters.

The field named ``I`` is a Bio-IFGT constraint-density field in a
biological observation window. It should not be read as identical to the
general IFGT variable I=f(1-C); it is a coarse-grained biological proxy for
local structure, differentiation, and retained bias.
"""

import argparse
import os
import tempfile
from pathlib import Path

import numpy as np

_CACHE_ROOT = Path(tempfile.gettempdir()) / "bio_ifgt_minimal_neural_field_cache"
os.environ.setdefault("MPLCONFIGDIR", str(_CACHE_ROOT / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(_CACHE_ROOT / "xdg"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Grid and runtime parameters.
GRID_SIZE = 128
STEPS = 800
DT = 0.08
SEED = 7
MODEL_VERSION = "v2_hierarchical"
SOURCE_MODE = "central_band"
ENABLE_GIF = True
GIF_EVERY = 10
GIF_FPS = 12

# DNA-like parameter set theta.
# These parameters constrain dynamics. They do not encode a completed form.
D_M = 0.45
LAMBDA_M = 0.030
SIGMA_M_STRENGTH = 0.20
SIGMA_M_BAND_WIDTH = 8
SOURCE_STRENGTH = 1.0
SOURCE_WIDTH = 0.035
Y_WIDTH = 0.35

D_I = 0.16
LAMBDA_I = 0.020
ALPHA = 0.09

THETA_N = 1.15
ETA_N = 0.030
SIGMOID_K = 8.0

ENABLE_EYE = True
EYE_MODE = "central_band_window"
ETA_B = 0.020
THETA_B = 0.55
ETA_E = 0.020
THETA_EN = 0.50
THETA_EB = 0.50
EYE_Y_WIDTH = 0.08
K_EYE = 20.0

PERTURBATION_SCALE = 1.0e-4


def laplacian(field):
    """Return a 2D Laplacian with edge-copy zero-flux boundaries."""
    padded = np.pad(field, pad_width=1, mode="edge")
    return (
        padded[2:, 1:-1]
        + padded[:-2, 1:-1]
        + padded[1:-1, 2:]
        + padded[1:-1, :-2]
        - 4.0 * field
    )


def sigmoid(z):
    """Stable logistic threshold function."""
    clipped = np.clip(-SIGMOID_K * z, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(clipped))


def eye_sigmoid(z):
    """Stable logistic threshold function for the eye-like field."""
    clipped = np.clip(-K_EYE * z, -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(clipped))


def make_sigma_m(grid_size, mode):
    """Create the morphogen source profile for the selected source mode."""
    if mode == "left_edge":
        sigma = np.zeros((grid_size, grid_size), dtype=float)
        y = np.linspace(-1.0, 1.0, grid_size)
        vertical_profile = np.exp(-(y / 0.65) ** 2)
        sigma[:, :SIGMA_M_BAND_WIDTH] = SIGMA_M_STRENGTH * vertical_profile[:, None]
        return sigma

    if mode == "central_band":
        coord = np.linspace(0.0, 1.0, grid_size)
        X, Y = np.meshgrid(coord, coord, indexing="xy")
        sigma = SOURCE_STRENGTH * np.exp(-((X - 0.5) ** 2) / (2.0 * SOURCE_WIDTH**2))
        y_taper = np.exp(-((Y - 0.5) ** 2) / (2.0 * Y_WIDTH**2))
        return sigma * y_taper

    supported = ("left_edge", "central_band")
    raise ValueError(f"Unsupported SOURCE_MODE {mode!r}. Use one of: {supported}")


def make_eye_window(grid_size, mode):
    """Create a positional window for toy eye-like commitment."""
    coord = np.linspace(0.0, 1.0, grid_size)
    X, Y = np.meshgrid(coord, coord, indexing="xy")

    if mode in ("central_band_window", "central_pair"):
        return np.exp(-((Y - 0.5) ** 2) / (2.0 * EYE_Y_WIDTH**2))

    if mode == "edge_pair":
        window_1 = np.exp(-((Y - 0.35) ** 2) / (2.0 * EYE_Y_WIDTH**2))
        window_2 = np.exp(-((Y - 0.65) ** 2) / (2.0 * EYE_Y_WIDTH**2))
        window = window_1 + window_2
        return window

    if mode == "single_pair":
        x_window = np.exp(-((X - 0.35) ** 2) / (2.0 * 0.18**2))
        window = np.exp(-((Y - 0.5) ** 2) / (2.0 * EYE_Y_WIDTH**2))
        return window * x_window

    supported = ("central_band_window", "central_pair", "edge_pair", "single_pair")
    raise ValueError(f"Unsupported EYE_MODE {mode!r}. Use one of: {supported}")


def gradient_magnitude(field):
    """Return normalized gradient magnitude for the constraint-density field."""
    grad_y, grad_x = np.gradient(field)
    G = np.sqrt(grad_x**2 + grad_y**2)
    return G / (float(np.max(G)) + 1.0e-8)


def normalize_for_plot(field):
    """Normalize a field to [0, 1] for RGB composition."""
    minimum = float(np.min(field))
    maximum = float(np.max(field))
    if maximum <= minimum:
        return np.zeros_like(field)
    return (field - minimum) / (maximum - minimum)


def save_field(field, path, title, cmap):
    """Save a single-field image with a colorbar."""
    fig, ax = plt.subplots(figsize=(5, 4.5), constrained_layout=True)
    image = ax.imshow(field, origin="lower", cmap=cmap)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_combined(M, I, N, path):
    """Save a compact RGB summary of all fields."""
    rgb = np.zeros((*M.shape, 3), dtype=float)
    rgb[..., 0] = normalize_for_plot(N)
    rgb[..., 1] = normalize_for_plot(I)
    rgb[..., 2] = normalize_for_plot(M)

    fig, ax = plt.subplots(figsize=(5, 4.5), constrained_layout=True)
    ax.imshow(rgb, origin="lower")
    ax.set_title("Combined fields: N red, I green, M blue")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_combined_with_eye(M, I, N, E, path):
    """Save RGB fields with eye-like commitment overlaid in white."""
    rgb = np.zeros((*M.shape, 3), dtype=float)
    rgb[..., 0] = normalize_for_plot(N)
    rgb[..., 1] = normalize_for_plot(I)
    rgb[..., 2] = normalize_for_plot(M)

    eye_mask = E > 0.5
    rgb[eye_mask] = np.array([1.0, 1.0, 1.0])

    fig, ax = plt.subplots(figsize=(5, 4.5), constrained_layout=True)
    ax.imshow(rgb, origin="lower")
    ax.set_title("Combined fields with E overlay")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(path, dpi=180)
    plt.close(fig)


def save_neural_eye_overlay(N, E, path):
    """Save neural commitment with an eye-like commitment contour."""
    fig, ax = plt.subplots(figsize=(5, 4.5), constrained_layout=True)
    image = ax.imshow(N, origin="lower", cmap="plasma", vmin=0.0, vmax=1.0)

    if np.max(E) > 0.5:
        ax.contour(E, levels=[0.5], colors="cyan", linewidths=1.5, origin="lower")

    ax.set_title("Neural commitment N with E > 0.5 contour")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    fig.savefig(path, dpi=180)
    plt.close(fig)


def render_frame(frame, limits):
    """Render one 2x2 GIF frame and return it as an RGB array."""
    step, M, I, N, E = frame
    fig, axes = plt.subplots(2, 2, figsize=(7, 6), constrained_layout=True)

    panels = (
        (axes[0, 0], M, "M morphogen", "viridis", limits["M"]),
        (axes[0, 1], I, "I constraint density", "magma", limits["I"]),
        (axes[1, 0], N, "N neural commitment", "plasma", (0.0, 1.0)),
        (axes[1, 1], N, "E over N", "plasma", (0.0, 1.0)),
    )

    for ax, field, title, cmap, (vmin, vmax) in panels:
        ax.imshow(field, origin="lower", cmap=cmap, vmin=vmin, vmax=vmax)
        ax.set_title(f"{title} | t={step}")
        ax.set_xticks([])
        ax.set_yticks([])

    if np.max(E) > 0.5:
        axes[1, 1].contour(E, levels=[0.5], colors="cyan", linewidths=1.2, origin="lower")
    else:
        axes[1, 1].imshow(E, origin="lower", cmap="cividis", vmin=0.0, vmax=1.0, alpha=0.65)

    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    rgb = rgba[:, :, :3].copy()
    plt.close(fig)
    return rgb


def save_gif(frames, path):
    """Save the time evolution as a 2x2-panel GIF."""
    if not frames:
        return None

    try:
        import imageio.v2 as imageio
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "GIF output requires imageio. Install requirements.txt or rerun with --no-gif."
        ) from exc

    limits = {
        "M": (0.0, max(float(np.max(frame[1])) for frame in frames)),
        "I": (0.0, max(float(np.max(frame[2])) for frame in frames)),
    }
    images = [render_frame(frame, limits) for frame in frames]
    imageio.mimsave(path, images, fps=GIF_FPS)
    return path


def parse_args():
    """Parse runtime options without changing the default paper outputs."""
    parser = argparse.ArgumentParser(
        description="Run the minimal Bio-IFGT neural-field toy model."
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=STEPS,
        help=f"number of finite-difference steps (default: {STEPS})",
    )
    parser.add_argument(
        "--grid-size",
        type=int,
        default=GRID_SIZE,
        help=f"grid size per dimension (default: {GRID_SIZE})",
    )
    parser.add_argument(
        "--source-mode",
        choices=("left_edge", "central_band"),
        default=SOURCE_MODE,
        help=f"morphogen source geometry (default: {SOURCE_MODE})",
    )
    parser.add_argument(
        "--eye-mode",
        choices=("central_band_window", "central_pair", "edge_pair", "single_pair"),
        default=EYE_MODE,
        help=f"toy eye-like positional window (default: {EYE_MODE})",
    )
    parser.add_argument(
        "--no-eye",
        action="store_true",
        help="disable the toy eye-like commitment field",
    )
    parser.add_argument(
        "--no-gif",
        action="store_true",
        help="skip GIF generation for faster checks",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "outputs",
        help="directory for PNG/GIF outputs",
    )
    return parser.parse_args()


def run_simulation(
    *,
    steps=STEPS,
    grid_size=GRID_SIZE,
    source_mode=SOURCE_MODE,
    eye_mode=EYE_MODE,
    enable_eye=ENABLE_EYE,
    enable_gif=ENABLE_GIF,
):
    """Run the explicit finite-difference simulation."""
    rng = np.random.default_rng(SEED)
    size = grid_size

    M = np.zeros((size, size), dtype=float)
    I = PERTURBATION_SCALE * rng.standard_normal((size, size))
    N = np.zeros((size, size), dtype=float)
    B = np.zeros((size, size), dtype=float)
    E = np.zeros((size, size), dtype=float)
    sigma_M = make_sigma_m(size, source_mode)
    eye_window = make_eye_window(size, eye_mode)
    frames = []

    for step in range(steps + 1):
        if enable_gif and step % GIF_EVERY == 0:
            frames.append((step, M.copy(), I.copy(), N.copy(), E.copy()))

        if step == steps:
            break

        M += DT * (D_M * laplacian(M) - LAMBDA_M * M + sigma_M)
        I += DT * (D_I * laplacian(I) - LAMBDA_I * I + ALPHA * M)

        neural_signal = sigmoid(I - THETA_N)
        N += ETA_N * neural_signal * (1.0 - N)
        N = np.clip(N, 0.0, 1.0)

        G_norm = gradient_magnitude(I)
        boundary_signal = sigmoid(G_norm - THETA_B)
        B += ETA_B * boundary_signal * (1.0 - B)
        B = np.clip(B, 0.0, 1.0)

        if enable_eye:
            eye_signal = (
                eye_sigmoid(N - THETA_EN)
                * eye_sigmoid(B - THETA_EB)
                * eye_window
            )
            E += ETA_E * eye_signal * (1.0 - E)
            E = np.clip(E, 0.0, 1.0)

    return M, I, N, B, E, frames


def print_summary(M, I, N, B, E, gif_path, args):
    """Print a short numerical summary."""
    neural_fraction = float(np.mean(N > 0.5))
    boundary_fraction = float(np.mean(B > 0.5))
    eye_fraction = float(np.mean(E > 0.5))
    print("Minimal neural-field toy simulation")
    print(f"model version: {MODEL_VERSION}")
    print(f"source mode: {args.source_mode}")
    print(f"eye enabled: {not args.no_eye}")
    print(f"eye mode: {args.eye_mode}")
    print(f"gif enabled: {not args.no_gif}")
    print(f"grid size: {args.grid_size} x {args.grid_size}")
    print(f"steps: {args.steps}")
    print(f"M mean/max: {np.mean(M):.6f} / {np.max(M):.6f}")
    print(f"I mean/max: {np.mean(I):.6f} / {np.max(I):.6f}")
    print(f"N mean/max: {np.mean(N):.6f} / {np.max(N):.6f}")
    print(f"B mean/max: {np.mean(B):.6f} / {np.max(B):.6f}")
    print(f"E mean/max: {np.mean(E):.6f} / {np.max(E):.6f}")
    print(f"fraction with N > 0.5: {neural_fraction:.6f}")
    print(f"fraction with B > 0.5: {boundary_fraction:.6f}")
    print(f"fraction with E > 0.5: {eye_fraction:.6f}")
    if gif_path is not None:
        print(f"gif: {gif_path}")


def main():
    args = parse_args()
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    M, I, N, B, E, frames = run_simulation(
        steps=args.steps,
        grid_size=args.grid_size,
        source_mode=args.source_mode,
        eye_mode=args.eye_mode,
        enable_eye=not args.no_eye,
        enable_gif=not args.no_gif,
    )

    suffix = args.source_mode
    v2_suffix = "v2"

    save_field(
        M,
        output_dir / f"morphogen_final_{suffix}.png",
        f"Morphogen field M ({args.source_mode})",
        "viridis",
    )
    save_field(
        I,
        output_dir / f"information_density_final_{suffix}.png",
        f"Constraint-density field I ({args.source_mode})",
        "magma",
    )
    save_field(
        N,
        output_dir / f"neural_commitment_final_{suffix}.png",
        f"Neural commitment N ({args.source_mode})",
        "plasma",
    )
    save_combined(M, I, N, output_dir / f"combined_fields_{suffix}.png")

    if not args.no_eye:
        save_field(
            E,
            output_dir / f"eye_commitment_final_{suffix}.png",
            f"Eye-like commitment E ({args.source_mode})",
            "cividis",
        )
        save_combined_with_eye(
            M,
            I,
            N,
            E,
            output_dir / f"combined_fields_with_eye_{suffix}.png",
        )
        save_neural_eye_overlay(
            N,
            E,
            output_dir / f"neural_eye_overlay_{suffix}.png",
        )

    save_field(M, output_dir / f"morphogen_final_{v2_suffix}.png", "Morphogen field M (v2)", "viridis")
    save_field(
        I,
        output_dir / f"information_density_final_{v2_suffix}.png",
        "Constraint-density field I (v2)",
        "magma",
    )
    save_field(
        N,
        output_dir / f"neural_commitment_final_{v2_suffix}.png",
        "Neural commitment N (v2)",
        "plasma",
    )
    save_field(
        B,
        output_dir / f"boundary_field_final_{v2_suffix}.png",
        "Boundary stabilization B (v2)",
        "cividis",
    )
    if not args.no_eye:
        save_field(
            E,
            output_dir / f"eye_commitment_final_{v2_suffix}.png",
            "Eye-like commitment E (v2)",
            "cividis",
        )
        save_combined_with_eye(
            M,
            I,
            N,
            E,
            output_dir / f"combined_fields_with_eye_{v2_suffix}.png",
        )
        save_neural_eye_overlay(N, E, output_dir / f"neural_eye_overlay_{v2_suffix}.png")

    gif_path = None
    if not args.no_gif:
        gif_path = save_gif(frames, output_dir / f"development_{MODEL_VERSION}.gif")

    print_summary(M, I, N, B, E, gif_path, args)
    print(f"outputs: {output_dir}")


if __name__ == "__main__":
    main()
