# Changelog

All notable changes to this repository will be documented in this file.

## Unreleased

- Added `bio-ifgt/`, a biological coarse-graining of IFGT/VED.
- Added a minimal neural-field toy simulation for morphogen diffusion,
  constraint-density formation, neural commitment, boundary stabilization,
  and secondary eye-like commitment.
- Clarified that Bio-IFGT variables are biological coarse-grained proxies and
  should not be directly identified with the general IFGT variables.

## 2026-05-11 — Vol.4 Reorganization and Framework Synchronization

### Added

- Added `00_overview.md` as a reader-facing map of the full VED framework.
- Added `correspondences.md` to preserve compact structural correspondences
  between VED and existing physical frameworks.
- Added `claims.md` to preserve stronger interpretive claims separately from
  the top-level README.
- Clarified the role of Vol.4 as the volume on Differential Horizon,
  divergence, renormalization, observational boundary, theory replacement,
  and limits.

### Changed

- Updated the framework overview to reflect the Vol.4 reorganization.
- Reframed complete closure as a boundary representation rather than an
  ordinary attainable state.
- Clarified that effective barrier parameters such as
  `\kappa_{B,\mathrm{eff}}` are projected or coarse-grained quantities,
  not fundamental external prohibitions.
- Softened public-facing claims by replacing overly definitive language with
  structural or framework-internal formulations.
- Moved strong claims about conservation laws, Newton's constant, and black
  hole singularities out of the main README and into `claims.md`.
- Moved compact correspondence tables out of the main README and into
  `correspondences.md`.
- Updated overview language from "established" to "structurally formulated"
  to avoid implying completed predictive validation.

### Fixed

- Corrected Markdown/LaTeX notation issues in the overview, including tensor
  indices and logarithmic spacing.
- Repaired display formatting for the Standard Model closure-geometry
  relation.
- Standardized notation around complete-closure limits, effective non-closure
  scales, and boundary representations.

### Notes

- This update does not introduce a new physical postulate.
- The single foundational axiom remains: **There is difference.**
- Vol.4 now functions as the conceptual and mathematical bridge explaining why
  complete closure appears only as a dynamic limit, observational boundary, or
  effective barrier in lower-level descriptions.

## Vol.4 — May 2026 (Second Edition)

Major structural revision across all 15 sections.

Core additions:

- §3: Reframed as "Physical Description as Pastified Texture";
  introduces trace formation
- §5: Differential Horizon reinterpreted as relational structure
- §7: Divergence reread as boundary signal and descriptive overextension
- §8: Renormalization reinterpreted as finite re-expression of boundary contact
- §10: Unresolved problems repositioned as local horizon-forms
- §11: Differential Horizon Principle updated; adds Local Horizons,
  Counterfactual Description, and Provisional Status
- §12: VED repositioned as open generative framework
- §13: Fully revised with degenerate manifold analysis, six observation
  windows, and reinterpretation as a local Differential Horizon

Central new vocabulary: registered difference, descriptive window,
pastified texture, trace formation, boundary signal, finite re-expression,
local horizon-form, open generative framework.

## v0.1.0

Initial public baseline repository structure.

- added bilingual top-level README files
- added overview, methodology, and open-problem documents
- added Vol.1-Vol.4 source materials and companion documents
- added initial figures and visual reference materials
- established initial licensing direction
