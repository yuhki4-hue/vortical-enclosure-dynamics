# Minimal Neural Field Toy Simulation

This directory contains a minimal illustrative toy model for the Bio-IFGT paper. It is not a biological claim and it is not a realistic model of embryogenesis.

The simulation shows how a simple DNA-like parameter set can produce a neural-like region through morphogen diffusion, biological constraint-density formation, thresholding, and attractor-like stabilization. It also includes a toy eye-like commitment field that can emerge from the neural field and boundary structure. The model does not encode a completed neural or eye shape.

The default `SOURCE_MODE = "central_band"` places the morphogen source near the center of the embryo-like domain. This produces a toy neural-plate-like region. This is still only a schematic illustration; it does not model real embryogenesis.

## Variables

- `M`: morphogen field.
- `I`: Bio-IFGT constraint-density field. This is a biological
  coarse-grained proxy for local structure, differentiation, and retained bias;
  it should not be identified directly with the general IFGT variable
  `I=f(1-C)`.
- `N`: neural commitment field.
- `B`: boundary/edge stabilization field derived from the gradient structure of `I`.
- `E`: eye-like commitment field.

## DNA-Like Parameter Set

DNA is represented only by parameters:

- `D_M`: morphogen diffusion coefficient.
- `lambda_M`: morphogen decay rate.
- `sigma_M`: morphogen source profile.
- `D_I`: constraint-density diffusion coefficient.
- `lambda_I`: constraint-density decay rate.
- `alpha`: coupling from morphogen to constraint density.
- `theta_N`: neural commitment threshold.
- `eta_N`: neural commitment update rate.
- `k`: sigmoid steepness.
- `MODEL_VERSION`: model label, currently `v2_hierarchical`.
- `ENABLE_GIF`: toggles GIF generation.
- `GIF_EVERY`: frame interval for GIF generation.
- `GIF_FPS`: GIF playback speed.
- `ENABLE_EYE`: toggles the toy eye-like commitment field.
- `EYE_MODE`: eye-window geometry, currently `central_band_window` by default.
- `eta_B`: boundary stabilization update rate.
- `theta_B`: threshold for normalized information-density gradient contribution to `B`.
- `eta_E`: eye-like commitment update rate.
- `theta_EN`: threshold for neural commitment contribution to `E`.
- `theta_EB`: threshold for boundary-field contribution to `E`.
- `eye_y_width`: width of the eye-like positional windows.
- `k_eye`: sigmoid steepness for eye-like thresholding.
- `SOURCE_MODE`: morphogen source geometry, either `left_edge` or `central_band`.

These parameters constrain the dynamics. They do not specify a completed final morphology.

## Source Modes

- `left_edge`: places a localized source near the left side of the domain.
- `central_band`: places a vertical Gaussian source band near the center of the domain, gently tapered along the vertical axis.

The conceptual point of `central_band` is that a parameterized source, diffusion, biological constraint-density formation, and thresholding can produce a stable central neural-like region without encoding that final region as a completed shape.

## v2 Hierarchy

The current model version is `v2_hierarchical`. Its structure is:

```text
M -> I -> N
I gradient -> B
N + B + positional window -> E
```

In words:

- `M` creates a morphogen field.
- `I` accumulates biological constraint density from `M`.
- `N` appears by thresholding `I`.
- `B` appears from the edge or gradient structure of `I`.
- `E` appears when `N` and `B` both exceed thresholds inside a positional window.

The conceptual point is that a small DNA-like parameter set does not encode neural or eye geometry directly. It defines sources, diffusion, decay, thresholds, and response rates. The visible structures emerge as stable outcomes of the field dynamics.

## Toy Eye-Like Commitment

The field `E` is not an encoded eye and is not a realistic eye-development model. It is a secondary toy commitment field. It is updated where:

- neural commitment `N` is high enough,
- the boundary field `B` is high enough,
- a coarse positional window is active.

With `EYE_MODE = "central_band_window"`, the positional window favors the middle of the vertical axis. The paired structure is not inserted by this window alone; it appears through the combination of the central window with the boundary field at the edges of the central neural plate. This can produce a left/right pair of eye-spot-like commitments near neural-field boundaries.

The conceptual point is that DNA-like parameters can specify rough conditions, while finer structure appears as a stable outcome of field dynamics and thresholding.

## Bio-IFGT Mapping

- `M` corresponds to a morphogen field.
- `I` corresponds to a Bio-IFGT constraint-density proxy.
- `N` corresponds to neural commitment.
- `B` corresponds to edge or boundary stabilization derived from the structure of `I`.
- `E` corresponds to a secondary eye-like commitment.
- Thresholding corresponds to a DNA-like conditional response regime.
- The final stable region corresponds to an attractor-like outcome.

## Run

From the Bio-IFGT directory:

```bash
python simulations/minimal_neural_field/simulate.py
```

From the top-level VED repository root:

```bash
python bio-ifgt/simulations/minimal_neural_field/simulate.py
```

The script writes PNG outputs to `simulations/minimal_neural_field/outputs/`
relative to the Bio-IFGT directory. From the top-level VED repository root,
the same outputs appear under
`bio-ifgt/simulations/minimal_neural_field/outputs/`.

For a faster smoke test without GIF generation:

```bash
python bio-ifgt/simulations/minimal_neural_field/simulate.py --steps 80 --no-gif
```

GIF output requires `imageio`; PNG-only runs can use `--no-gif`.

Useful runtime options:

- `--steps N`: override the number of finite-difference steps.
- `--grid-size N`: override the square grid size.
- `--source-mode {left_edge,central_band}`: choose the morphogen source.
- `--eye-mode {central_band_window,central_pair,edge_pair,single_pair}`: choose the toy eye window. `central_pair` is retained as a backward-compatible alias for `central_band_window`.
- `--no-eye`: disable the toy eye-like commitment field.
- `--no-gif`: skip GIF generation.
- `--output-dir PATH`: write outputs to a custom directory.

The script also writes v2 outputs:

- `morphogen_final_v2.png`
- `information_density_final_v2.png`
- `neural_commitment_final_v2.png`
- `boundary_field_final_v2.png`
- `eye_commitment_final_v2.png`
- `neural_eye_overlay_v2.png`
- `combined_fields_with_eye_v2.png`
- `development_v2_hierarchical.gif`

For backward comparison, output filenames also include the selected source mode, for example:

- `morphogen_final_central_band.png`
- `information_density_final_central_band.png`
- `neural_commitment_final_central_band.png`
- `combined_fields_central_band.png`
- `eye_commitment_final_central_band.png`
- `combined_fields_with_eye_central_band.png`
- `neural_eye_overlay_central_band.png`
