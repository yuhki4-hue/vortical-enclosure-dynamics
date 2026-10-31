# Bio-IFGT core revision implementation Phase 02 — formal equation role / paper-code correspondence

## 0. Status

- Implementation Phase 02: **COMPLETE**
- Bio-IFGT audit: **CLOSED**
- Final dispositions: **FROZEN**
- Bio-IFGT core revision: **IN PROGRESS**
- Phase 01 source identity / notation alignment: **COMPLETE**
- Phase 03 stability / attractor / life wording: **NOT STARTED**
- displayed equation change: **0**
- simulation code / parameter / tracked output change: **0**
- new equation / notation family / theory / bridge: **0**
- upstream VED / IFGT audit reopening: **NO**

## 1. Authority

Primary authority is the [Phase 07 final audit record](07_final_audit_record_v1.0_ja.md).
The [Phase 01 implementation record](implementation_phase_01_source_identity_v0.1_ja.md) is the implemented baseline.
The [Phase 06 candidates](06_revision_candidates_v0.1_ja.md),
[Phase 05 execution audit](05_simulation_and_empirical_correspondence_audit_v0.1_ja.md),
[Phase 02 role audit](02_equation_role_and_biological_role_audit_v0.1_ja.md), and
[Phase 01 inventory](01_equation_and_symbol_inventory_v0.1_ja.md) supply trace evidence.
Upstream VED / IFGT dispositions remain closed and unchanged.

## 2. Scope

This phase implements only:

- formal equation role and representation/domain context;
- continuous paper form versus source-specific finite execution;
- actual update order, DT scope, clipping, and threshold-helper correspondence;
- state, intermediate, diagnostic, and visualization roles;
- compact staged sequence versus executable dependency.

It does not implement the later stability, attractor, life-identification, empirical, cross-scale, downstream, figure, or PDF alignment phases.
No displayed expression or executable operation is changed.

The operative guards are:

- continuous equation is not the finite update implementation;
- paper summary order is not execution dependency;
- diagnostic quantity is not state variable;
- navigation arrow is not causal dependency;
- source-local formal relation is not code-integrated variable.

## 3. Final dispositions implemented

The table records the Phase-02 aspect of each frozen final disposition. BIO-FD-007/008 were identity-separated in Phase 01 and receive their execution-role completion here.

| BIO-FD | Source location | Change made | Equation changed? | OPEN preserved? |
|---|---|---|---|---|
| BIO-FD-007 | EN/JA toy sections; simulation/result prose; simulation README | raw G, globally normalized G_norm input, and accumulated B state are separated in the actual update description | NO | YES — no new paper/code identity or biological boundary map |
| BIO-FD-008 | EN/JA toy sections; simulation README | paper S remains symbolic; code sigmoid/eye_sigmoid, existing slopes, and exponential clipping are documented as execution variants | NO | YES — no common replacement function supplied |
| BIO-FD-013 | EN/JA Formal Mapping and Core; Bio README | state/domain declarations, balance relation, and constitutive/effective relations retain their formal content | NO | YES — physical/biological carrier identification is not added |
| BIO-FD-014 | EN/JA Formal Mapping, Core, Development; JA working sources | continuum representation, differentiability, chosen Phi, and effective/conditional roles are locally stated | NO | YES — unspecified potential and operational map remain unresolved |
| BIO-FD-015 | EN/JA Formal Mapping and Life; Bio README | tau relation is identified as an accumulation definition relative to external t, not a finite code update | NO | YES — clock calibration remains OPEN |
| BIO-FD-017 | EN/JA Development and Life; JA working Development | reaction–diffusion is a continuous coarse-grained evolution relation; state-space formula is a generic evolution rule | NO | YES — biological mechanism and life-region existence are not supplied |
| BIO-FD-049 | EN/JA toy sections; simulation README | existing PDE forms, per-step updates, intermediates, and diagnostics are retained as source-specific model content | NO | YES — formal-to-biological translations remain OPEN |
| BIO-FD-050 | EN/JA toy sections; simulation results; simulation README | prescribed source, new M to I order, new I to N/G_norm/B, new N/B to E, DT scope, clipping, and schedule are stated side by side | NO | YES — execution facts are not promoted to new equations |
| BIO-FD-051 | EN/JA toy and result sections; simulation README; Bio README | compact M/I/N/B/E order is separated from the branching actual dependencies; direct N-to-B input is explicitly absent | NO | YES — no new canonical chain or arrow calculus |
| BIO-FD-052 | EN/JA toy and result sections; Bio README | uniform causal reading is excluded while the staged/navigation use of the compact sequence is retained | NO | YES — quasi-closure and biological generation are not established |
| BIO-FD-053 | EN/JA toy sections | Phi/J toy statements are marked formal or interpretive rather than literal independently integrated code variables | NO | YES — Phi/J/quasi-closure mapping remains OPEN |

BIO-FD-054 has a later time-horizon/stability and biological-boundary component. This phase records only the already-authorized G/G_norm/B execution distinction under BIO-FD-007/049/050; it does not claim full BIO-FD-054 implementation.

## 4. Files changed

Current-facing sources:

- [Bio README](../../bio-ifgt/README.md)
- [EN Formal Mapping](../../bio-ifgt/sections/formal_mapping.tex)
- [EN Core Equations](../../bio-ifgt/sections/core_equations.tex)
- [EN Development](../../bio-ifgt/sections/development_morphogenesis.tex)
- [EN Life Attractor](../../bio-ifgt/sections/life_attractor.tex)
- [EN Minimal Developmental Simulation](../../bio-ifgt/sections/minimal_developmental_simulation.tex)
- [EN Simulation Results](../../bio-ifgt/sections/simulation_results_visualization.tex)
- [self-contained JA manuscript](../../bio-ifgt/main_ja.tex)
- [simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md)

Working-source notes:

- [JA working Formal Mapping](../../bio-ifgt/sections_ja/formal_mapping_ja.md)
- [JA working Core Equations](../../bio-ifgt/sections_ja/core_equations_ja.md)
- [JA working Development](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md)

Audit status / traceability:

- [Bio-IFGT audit README](README_ja.md)
- this implementation record

There is no separate minimal-developmental-simulation working Markdown file in the current tree. No substitute source was invented.

## 5. Core equation role implementation

The EN and self-contained JA manuscripts now state that:

- I and J displays declare continuum fields and domains;
- the continuity equation is a balance relation;
- flow and potential expressions are constitutive/effective relations conditional on the selected potential functional and spatial representation;
- internal tau is an accumulation definition relative to t;
- reaction–diffusion and state-space evolution are formal model relations rather than the finite toy loop.

The JA working Formal/Core/Development files carry equivalent role notes while retaining their working-source forms.

## 6. M / I paper-code correspondence

The displayed M and I relations remain continuous model forms. The execution prose now records that the finite code:

1. uses an imposed source profile for M;
2. performs an explicit finite update of M;
3. uses the newly updated M in the I update within the same loop;
4. applies DT to M and I.

This is an execution-order statement, not an exact-PDE-solver claim and not a new equation.

## 7. N / B / E implementation correspondence

The current N, B, and E rules remain the displayed symbolic per-step forms. Execution prose records:

- no DT multiplier is used for these three code updates;
- N is updated and clipped before G_norm/B;
- B is updated from the normalized gradient-derived input and clipped;
- E uses the current updated N and B, the explicit positional window, and eye_sigmoid, then is clipped;
- the loop is ordered rather than simultaneous.

No update logic, rate, threshold, or bound changed.

## 8. G / G_norm / B separation

The paper display remains raw G as gradient magnitude. The code computes that raw magnitude internally, returns its global normalization as G_norm, and feeds G_norm to the B update. B is a separately accumulated state. The result prose and B caption now describe this source-specific execution relationship without replacing raw G in the paper equation.

## 9. Compact chain / actual dependency

All current displayed M/I/N/B/E compact sequences are retained. Each current-facing occurrence now has a local scope note:

- the sequence is staged presentation/navigation;
- source updates M;
- new M feeds I;
- I separately feeds N and the raw-to-normalized gradient route to B;
- N, B, and the positional window feed E;
- N is not a direct B input.

No new canonical equation chain or formal arrow semantics was introduced.

## 10. J / Phi / toy correspondence

The continuum J/Phi relations remain intact. The toy-source notes now state that their use near the finite model is formal or interpretive correspondence. The code does not directly integrate independent J or Phi arrays, and no literal one-to-one or quasi-closure map was supplied.

## 11. Diagnostics / visualization

The following roles are now explicit:

- M/I/N/B/E: finite model states;
- G_norm: normalized model intermediate and B input, not display-only;
- mean, maximum, and fraction above 0.5: numerical run diagnostics;
- contours and RGB normalization: visualization transforms.

The diagnostic/display quantities are not asserted to be independently measured biological observables.

## 12. Working / canonical version handling

Canonical EN TeX, self-contained JA TeX, JA working Markdown, and executable code remain separate authorities as fixed in Phase 01. Working sources receive role annotations rather than silent canonicalization. Paper equations are not rewritten to reproduce every code operation, and code is not rewritten to imitate the symbolic paper forms.

## 13. Equation immutability check

Before the Phase-02 edits, displayed equation/align/bracket/double-dollar blocks in all 33 Bio TeX and Markdown sources were hashed. After editing, all per-file counts and hashes match:

- displayed equation added / removed / changed: 0 / 0 / 0;
- coefficient, sign, operator, exponent, index, variable, functional form: unchanged;
- formula semantics changed: NO.

Simulation immutability:

- simulate.py SHA-256 remains f98e10a807a53b1448fdb9e994864c7448f5b07e61e89bf73abfce0401ee8d8e;
- requirements, all pre-existing output PNGs, main.pdf, and main_ja.pdf match their pre-edit hashes;
- code logic, parameters, tracked output, and distribution PDF changes: 0.

## 14. Validation

- source-path existence: PASS
- Phase-02 final-disposition trace: PASS
- displayed-math block comparison: PASS, 33 / 33 unchanged
- simulation / requirements / output / PDF byte hashes: PASS, unchanged
- compact-chain occurrence scan and local role labels: PASS
- direct N-to-B wording check: PASS — all current occurrences distinguish staging from direct input
- EN/JA major role and execution parity: PASS
- Markdown fences / display delimiters / tables: PASS
- TeX environment balance: PASS
- temporary EN compile: PASS, 29 pages
- temporary JA compile: PASS, 22 pages; existing font-size substitution warnings only
- tracked PDFs updated: NO
- relative links in changed Markdown / audit records: PASS
- git diff --check: PASS
- temporary/build junk in repository: none introduced

The first sandboxed JA compile attempt was blocked by a non-writable LuaTeX font cache. A compile using the existing font cache completed successfully; this was an environment constraint, not a source error.

## 15. Next phase

Next implementation phase is **Phase 03 — stability / attractor / life wording**.
It is **NOT STARTED**. This record does not authorize beginning it.
