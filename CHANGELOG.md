# Changelog

All notable changes to this repository will be documented in this file.

## Unreleased

- Archived the closed theorem/proof anatomy experimental series under
  `notes/theorem_proof_anatomy_experiment/`, with a reader-facing archive
  README, final experimental record, source architecture, source map, and
  internal audit; preserved negative results and retired terminology as
  historical records, made no new proof-theory/framework claim, and updated
  relative links after the move.
- Added `stochastic-quantization/`, an exploratory quantitative working-note
  module for a χ-layer bridge from VED/IFGT closure dynamics to stochastic
  quantization, including bilingual READMEs, reproducible Python scripts, and
  generated figures for propagator, emergent light-cone, Collins two-field, and
  re-addressing gauge-sector probes.
- Added `dimensionality-working-note/`, a working-note module on dimension as
  effective rank of persistent difference structure, preserving failed routes,
  exploratory scripts, Betti/topological verification notes, and the open
  question of a VED account of `3+1` dimensionality.
- Added Dimensionality Working Note II materials and v24.1-v24.3 diagnostic
  runs, including headroom, extended-epoch, rule-decomposition, phase
  classification, and band-fate audit tools for BSW/MRW route testing.
- Added `lattice_anchor_ext.py` and v24.3 robust-BSW `-log(S)` weight exports
  for non-periodic, size-matched, empirical-weight `d_cal` anchor
  recalibration.
- Added v24.2e robust-BSW weight exports and faithful-convention `d_cal`
  recalibration; updated 2b phase-classifier calibration to use same-run
  old-classifier agreement on mechanically selected unimodal runs, yielding a
  reproducing region and standard setting for subsequent 2c adjudication.
- Added Campaign A cycle-individual tracking runs for the dimensionality
  working note, including TD/TL2 lifetime, death-attribution, phase
  classification, and repair/turnover diagnostic outputs.
- Added 4000-epoch TD seed-5 Campaign A reconciliation logs and analysis,
  linking the 2c trajectory to repair/turnover reinterpretation via
  phase-dependent cycle-hazard modulation.
- Added `campA_phase_hazard.py` and the TD seed-7 4000-epoch phase-hazard
  confirmation run for Campaign A, preserving the shedding-culling result
  while exposing seed-dependent consolidation age selectivity.
- Completed TD 4000-epoch Campaign A phase-hazard confirmation for seeds
  10/15/21/33, reproducing shedding culling in 5/5 confirmation seeds and
  consolidation age-selectivity in 4/5.
- Refined the Campaign A phase-hazard interpretation: pooled results indicate
  that old-cycle hazard attenuation belongs to contraction broadly, while
  consolidation differs from shedding by lower hazard level rather than a
  unique age-gradient.
- Added `campA_insertion_hazard.py` and updated Dimensionality Working Note II
  through §7.7.3: absolute-hazard decomposition re-identifies the age effect
  as growth-phase old-cycle culling, and the holdout insertion-pressure audit
  yields partial decomposition rather than full mediation.
- Registered the next Dimensionality Working Note II step as an edge
  flux-fate audit, prioritizing pure-read edge-level feeding, maintenance
  margin, shared-edge loss, and overlap-unraveling diagnostics before further
  TS-cell or `d_new(V)` work.
- Added `growth_flux_ledger.py` and TD 4000-epoch Campaign A flux-ledger runs
  for seeds 5/7/10/15/21/33; verified pure-read behavior against existing
  Campaign A cycle/alive logs and preserved edge-level ledger plus cycle-edge
  outputs for §7.7.4.
- Added `dimensionality-working-note/reports/` as a public summary layer for
  the current dimensionality-selection experiment cycle, with GitHub Pages
  routing from the dimensionality index and README.
- Linked the stochastic-quantization module from the top-level READMEs,
  Navigation Layer, Concept Map, Reading Paths, Theory Relationship Map,
  Simulation Reading Guide, and GitHub Pages entry point.
- Linked the dimensionality working note from the top-level READMEs, Navigation
  Layer, Concept Map, Reading Paths, Theory Relationship Map, Simulation
  Reading Guide, and GitHub Pages entry point.
- Added lightweight HTML reading views for the stochastic-quantization English
  and Japanese READMEs, using relative links to existing figure PNGs for easier
  GitHub Pages browsing.
- Added `docs/ai_spine/requirements.txt` and made the AI Spine schema check
  self-describing when optional `jsonschema` validation is unavailable.
- Localized AI Spine validation report statuses so one failing check no longer
  turns unrelated checks into ambiguous global `see_errors` entries; added an
  explicit `layer3_absence` check.
- Added fast/slow interpretation guardrails distinguishing Kahneman System
  1/2, AI engineering inference protocols, System 0/1/2/3 classifications, and
  VED/SSO structural speed-scale organization.
- Added LLM interpretation cautions: fast token generation should not be read
  as fast-layer dominance; Transformer-based LLMs may be read as
  System-3-like social-symbolic sedimentation appearing through a
  System-1-like interface.
- Added intelligence-locus caution: the output site is not the same as the
  intelligence locus.
- Added `docs/navigation/constraint_dynamics.md` to clarify constraint as
  trajectory-shaping across physical barriers, probabilistic biases,
  biological viability conditions, cognitive stopping structures, and social
  consensus mechanisms.
- Added GitHub Pages preparation files: root `.nojekyll`, a minimal static
  `index.html`, `robots.txt`, and an AI Spine directory index so
  `docs/ai_spine/spine.json` can be served directly as static JSON.
- Added explicit GitHub Pages and direct AI Spine JSON links to the English and
  Japanese README entry layers for AI readers that cannot reliably traverse the
  GitHub UI.
- Added `docs/ai_spine/` as an AI-readable calibration layer with
  machine-validated Layer 0-1 data, generated canonical derivation-order
  outputs, and an explicit policy that Layer 2 remains advisory and Layer 3 is
  absent.
- Added typed canonical-order metadata distinguishing `difference`, closure
  degree `C_ij`, gradient, flow, vortex, enclosure, and non-closure by
  `kind` and `derivation_role`.
- Separated closure degree `C_ij` from the causal log in the AI Spine and
  navigation entry text: `C_ij` is the rank-1 formal variable, while the causal
  log is the off-backbone accumulated trace of `C_ij`.
- Added non-generative validated relations for `c_ij -> causal_log`
  (`accumulation_structure`) and `c_ij -> information_field`
  (`structural_extension_of`) so IFGT is calibrated as a structure-layer
  extension rather than the next VED core rank.
- Reframed the English and Japanese README entry layers around a positive
  definition of VED as a generative structural framework beginning from the
  single axiom of difference.
- Updated the README and navigation layer to clarify that the causal log
  should not be fused with closure degree `C_ij` or treated as a second axiom.
- Replaced the AI summary test template with an observed test log covering GPT,
  Grok, and Gemini summary behavior, residual misreadings, and applied fixes.
- Added navigation documents for the VED generative sequence and for preventing
  reduction to complex-systems, dissipative-structure, or autopoiesis
  categories.
- Strengthened non-closure guidance by clarifying that absolute closure is
  structurally unreachable and that non-closure is constitutive rather than a
  defect or unfinished remainder.
- Added a top-level Navigation Layer to the English and Japanese README files,
  including reader-orientation guidance and links to concept, translation,
  theory-relationship, reading-path, simulation, and misreading guides.
- Added `docs/navigation/` as a conceptual navigation layer for human
  researchers and AI summarizers.
- Added navigation guides for concept mapping, vocabulary translation, reading
  paths, Vol.4 simulation interpretation, and common misreadings.
- Added cautious comparison guides for Enactivism, FEP, Predictive Processing,
  IIT, and Global Workspace-type models, framing them as theory relationships
  without equivalence or replacement claims.
- Added `bio-ifgt/`, a biological coarse-graining of IFGT/VED.
- Added a minimal neural-field toy simulation for morphogen diffusion,
  constraint-density formation, neural commitment, boundary stabilization,
  and secondary eye-like commitment.
- Clarified that Bio-IFGT variables are biological coarse-grained proxies and
  should not be directly identified with the general IFGT variables.
- Added `conceptual-topography/`, a cognitive and social application layer of
  IFGT/VED.
- Added a field-theoretic account of conceptual landscapes, token-field
  coupling, sedimented attractors, understanding as traversal-cost reduction,
  and social conceptual synchronization.
- Aligned Conceptual Topography with the revised closure framework by treating
  conceptual variables as cognitive-window projections and effective barrier
  terms as coarse-grained resistance rather than fundamental prohibitions.
- Added `consciousness/`, an application-layer account of consciousness as
  temporal non-closure, speed-scale orchestration, and cross-scale log
  referencing.
- Aligned the consciousness manuscript with the revised VED closure framework by
  treating consciousness as an opening regime rather than a generated object,
  using projected IFGT variables and the local log-referencing flow
  `J_{\log}`.
- Introduced projection as the fourth IFGT primitive in the consciousness
  manuscript, clarified projected uses of IFGT variables, and distinguished the
  structural use of projection from the psychological sense.
- Aligned the consciousness and intelligence manuscripts by treating the
  consciousness window and the intelligence-layer horizon as different
  projected windows of the same differential-development structure.
- Added `intelligence-part1/`, the first intelligence-layer paper in the
  VED/IFGT application series.
- Added English and Japanese LaTeX manuscripts, compiled PDFs, references, and
  bilingual figure sets for Intelligence Part I.
- Framed intelligence as a non-closed dynamical phenomenon constrained by
  connected state space, temporal ordering, global constraint `\Phi`, and a
  local horizon-form requiring externalized stopping structures.
- Added cross-domain structural comparison between slime mold dynamics and
  Transformer layer dynamics under the three minimal axioms.
- Added `intelligence-part2/`, the second intelligence-layer paper in the
  VED/IFGT application series.
- Added Japanese and English TeX manuscripts, appendices, source Markdown,
  bilingual figure sets, detailed figure-caption notes, and tracked PDF entry
  points for Intelligence Part II.
- Framed Intelligence Part II around inferential non-closure, externalized
  stopping, emergent stopping layers `L_E`, and historical stopping-operation
  systems such as religion, science, and social consensus.
- Linked available Japanese PDFs from the top-level README for Bio-IFGT,
  consciousness, Intelligence Part I, and Intelligence Part II.
- Flattened Intelligence Part II figure PDFs against a white background for more
  stable rendering in GitHub's PDF preview.

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
