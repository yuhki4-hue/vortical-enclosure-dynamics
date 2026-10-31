# Minimal Neural Field Toy Simulation

This directory contains a minimal illustrative toy model for the Bio-IFGT paper. It is not a biological claim and it is not a realistic model of embryogenesis.

The simulation shows how a simple DNA-like parameter set can produce a reproducible finite-horizon neural-like model region through a morphogen-like field, model constraint-density formation, and thresholding. It also includes a toy eye-like commitment field. The model does not encode a completed neural or eye output array, although its source profile and positional window supply coarse spatial information; its finite output is not a stationary-attractor, biological-stability, or empirical-validation result.

The default `SOURCE_MODE = "central_band"` places the morphogen source near the center of the embryo-like domain. This produces a toy neural-plate-like region. This is still only a schematic illustration; it does not model real embryogenesis.

## Execution and notation authority

`simulate.py` is the execution authority for the current finite model. The manuscript supplies the symbolic toy equations; it is not a line-by-line specification of every normalization or threshold helper in the code. The code arrays `M`, `I`, `N`, `B`, and `E` are source-local finite states. In particular, the code does not directly integrate the continuum Bio-IFGT current `J` or potential `Phi`, and its loop step/`DT` is not the Bio internal variable `tau` or a calibrated biological time.

The manuscript's `G` denotes the raw magnitude of the gradient of `I`. The helper `gradient_magnitude` computes that raw magnitude internally and returns a globally normalized value, used in the loop as `G_norm`; `B` is then an accumulated state updated from that normalized input. These three objects are not interchangeable. Similarly, the paper's symbolic `S(z)` is represented by two code functions: `sigmoid` uses `SIGMOID_K = 8`, while `eye_sigmoid` uses `K_EYE = 20`; both also clip exponential arguments for numerical execution.

The manuscript's `M` and `I` equations are continuous model forms; this script uses source-specific explicit finite updates rather than claiming an exact PDE solver. In each loop, `M` is updated first and the new `M` is used for `I`. The new `I` updates `N` and separately produces `G_norm` for `B`; the new `N` and `B`, plus `eye_window`, then update `E`. `DT` multiplies only the `M` and `I` updates. The `N`, `B`, and `E` accumulation rules use their own per-step rates, and all three are clipped to `[0, 1]`. This ordered execution is not a simultaneous update.

## Variables

- `M`: morphogen field.
- `I`: Bio-IFGT constraint-density field. This is a proposed model proxy for local structure, differentiation, and retained bias, not an operationally calibrated biological observable;
  it should not be identified directly with the general IFGT variable
  `I=f(1-C)`.
- `N`: neural-like model commitment field.
- `B`: accumulated state driven by the normalized gradient structure of `I`; at the reported horizon it can highlight boundary-like bands, but it is not an instantaneous or permanent biological boundary.
- `E`: eye-like model commitment field.

## DNA-Like Parameter Set

DNA-like constraints are represented abstractly by parameters; the code does not implement a genotype-to-parameter map or establish parameter provenance:

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

The conceptual point of `central_band` is that a parameterized source, diffusion, model constraint-density formation, and thresholding can produce a reproducible central neural-like pattern at the reported finite horizon without encoding that final region as a completed array. The source geometry is nevertheless prescribed and influences its location.

## v2 Hierarchy

The current model version is `v2_hierarchical`. Its structure is:

```text
M -> I -> N
I gradient -> B
N + B + positional window -> E
```

This block is a compact dependency summary for the finite code, not a biological causal chain. There is no direct `N -> B` input: `N` precedes `B` in the loop, while `B` receives the normalized gradient-derived input from `I`.

In words:

- `M` creates a morphogen field.
- `I` accumulates model constraint density from `M`.
- `N` appears by thresholding `I`.
- `B` appears from the edge or gradient structure of `I`.
- `E` appears when `N` and `B` both exceed thresholds inside a positional window.

The conceptual point is that a small DNA-like parameter set does not encode the completed neural- or eye-like output array directly. It does define source geometry, diffusion, decay, thresholds, response rates, and an eye positional window. The visible structures are reproducible finite-horizon model outcomes under those constraints; they are not geometry-free emergence, stationary solutions, or evidence of biological robustness.

## State, intermediate, diagnostic, and display roles

- `M`, `I`, `N`, `B`, and `E` are finite model states.
- `G_norm` is a normalized model intermediate and directly feeds the `B` update; it is not display-only.
- Printed means, maxima, and fractions above `0.5` are numerical run diagnostics.
- Contours and RGB normalization are visualization transforms and do not update the state.

These diagnostics and display transforms are not, by themselves, biological observables.

## Toy Eye-Like Commitment

The field `E` is not an encoded eye and is not a realistic eye-development model. It is a secondary toy commitment field. It is updated where:

- neural commitment `N` is high enough,
- the boundary field `B` is high enough,
- a coarse positional window is active.

With `EYE_MODE = "central_band_window"`, the positional window supplies coarse localization by favoring the middle of the vertical axis. In the audited default output, two relatively bright lobes are visible, but central `E` values are nonzero and the `E > 0.5` mask is one connected component. The result therefore does not establish two independent eye structures. Its localization is strongly window-dependent, and disabling the eye pathway gives `E = 0`; the code does not preload the completed final array.

The conceptual point is that DNA-like parameters can specify rough conditions, while finer model structure appears at the reported finite horizon through field dynamics and thresholding.

## Bio-IFGT Mapping

- `M` is a morphogen-like model field.
- `I` is the toy proxy for Bio-IFGT constraint density.
- `N` is a neural-like commitment label.
- `B` is a gradient-sensitive accumulated state with a boundary-like reading, not a membrane or organism boundary.
- `E` is a secondary eye-like commitment label under an explicit positional gate.
- Thresholding has a DNA-like conditional-response interpretation.
- The reported finite-horizon region permits an attractor-like reading; no formal basin, asymptotic stability, or biological life-region membership is established.

These mappings are qualitative model analogies, not operational biological identifications. No external biological dataset, units/calibration, or variable-to-observable map is used by the current simulation.

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

The seven tracked PNGs listed above were reproduced pixel-for-pixel in the audit environment, although their encoded files were not byte-identical. The historical alternate GIF lineage remains unresolved; neither provenance statement upgrades the outputs from model-local numerical artifacts to biological observations.

For backward comparison, output filenames also include the selected source mode, for example:

- `morphogen_final_central_band.png`
- `information_density_final_central_band.png`
- `neural_commitment_final_central_band.png`
- `combined_fields_central_band.png`
- `eye_commitment_final_central_band.png`
- `combined_fields_with_eye_central_band.png`
- `neural_eye_overlay_central_band.png`
