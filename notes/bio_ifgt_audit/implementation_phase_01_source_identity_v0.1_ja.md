# Bio-IFGT core revision implementation Phase 01 — source identity / notation alignment

## 0. Status

- Implementation Phase 01: **COMPLETE**
- Bio-IFGT audit: **CLOSED**
- Final dispositions: **FROZEN**
- Bio-IFGT core revision: **IN PROGRESS**
- Phase 02 formal equation role / paper-code correspondence: **NOT STARTED**
- displayed equation change: **0**
- new equation / notation family / theory / bridge: **0**
- upstream VED / IFGT audit reopening: **NO**

## 1. Authority

Primary authority is [Phase 07 final audit record](07_final_audit_record_v1.0_ja.md), especially BIO-FD-001–012.
[Phase 06 candidates](06_revision_candidates_v0.1_ja.md), [Phase 05 execution audit](05_simulation_and_empirical_correspondence_audit_v0.1_ja.md),
[Phase 01 inventory](01_equation_and_symbol_inventory_v0.1_ja.md), and the intervening Phase 00–04 records are trace support only.
Upstream VED / IFGT authority remains closed and unchanged.

## 2. Scope

This phase implements only source-local identity, notation reuse, source-version status, and artifact authority.
It does not implement the later formal-role, stability, biological-identification, empirical-correspondence,
cross-scale, downstream-attribution, figure, or PDF synchronization dispositions.
All changes are prose notes outside displayed equations. Current symbols are retained rather than renamed.

## 3. Final dispositions implemented

| BIO-FD | Source location | Change made | Equation changed? | OPEN preserved? |
|---|---|---|---|---|
| BIO-FD-001 | Bio README; EN/JA Formal Mapping; EN/JA toy description; simulation README; JA working Formal/Core | IFGT, Bio continuum, toy field, and code-array \(I\) are source-local; shared glyph is not carrier identity | NO | YES — operational / carrier map remains OPEN |
| BIO-FD-002 | Bio README; EN/JA Formal Mapping; EN/JA toy description; simulation README | VED \(J_{ij}\), continuum Bio \(\mathbf J\), working plain \(J\), and code non-integration are separated | NO | YES — event-to-current and finite/continuum maps remain OPEN |
| BIO-FD-003 | Bio README; EN/JA Formal Mapping and Life; JA working Life/Core | upstream density uses are separated from Bio progression forms \(\rho(I,\mathbf J)\) and \(\rho(x)\); exact relation between the two Bio functionals remains unspecified | NO | YES — functional and calibration maps remain OPEN |
| BIO-FD-004 | Bio README; EN/JA Core; JA working Core/Development; simulation README | Bio balance source, gene-related reading, toy \(\sigma_M\), and upstream \(\sigma\) uses are distinguished | NO | YES — biological source mechanism and upstream translation remain OPEN |
| BIO-FD-005 | Bio README; EN/JA Formal Mapping and toy description; simulation README | external \(t\), interpretive Bio \(\tau\), upstream time objects, loop step, and `DT` are separated | NO | YES — clock / duration map remains OPEN |
| BIO-FD-006 | Bio README; EN/JA Formal Mapping, Gene, and Life; JA working Formal/Gene/Life | \(\Phi[I]\), vector \(\mathbf F\), response \(F_k\), and evolution field \(F(x;\theta)\) are distinguished by signature and domain; code absence of independent \(\Phi/\mathbf J\) arrays is stated | NO | YES — potential/code and cross-layer maps remain OPEN |
| BIO-FD-007 | Bio README; EN/JA toy description; simulation README | paper raw \(G\), code normalized input `G_norm`, and accumulated state \(B\) are separated | NO | YES — paper/code interpretation remains scoped, not unified |
| BIO-FD-008 | Bio README; EN/JA toy description; simulation README | symbolic paper \(S(z)\) is separated from `sigmoid` / `eye_sigmoid`, including their existing steepness constants and clipping | NO | YES — no identity or replacement formula supplied |
| BIO-FD-009 | Bio README; JA working Gene and Development | canonical signatures with \(\theta\) and working signatures omitting it are recorded as versioned variants without silent completion | NO | YES — omission intent remains unresolved |
| BIO-FD-010 | Bio README; JA working notes | EN TeX, self-contained JA TeX, working Markdown, execution source, and PDFs/PNGs receive distinct authority roles | NO | YES — distribution freshness beyond the existing audit is not inferred |
| BIO-FD-011 | Bio README; JA working Intelligence | conditional canonical probability form and repeated-square working form are preserved; typo/shorthand/alternative intent is explicitly unresolved | NO | YES — source-version intent remains OPEN |
| BIO-FD-012 | Bio README; EN/JA Gene, Life, and toy notes | local collisions for \(N,B,G,x,D,\theta,A,C,E,S,k\) are indexed by source role without global renaming | NO | YES — shared glyphs are not converted into maps |

## 4. Files changed

Current-facing theory / navigation:

- [Bio README](../../bio-ifgt/README.md)
- [EN Formal Mapping](../../bio-ifgt/sections/formal_mapping.tex)
- [EN Core Equations](../../bio-ifgt/sections/core_equations.tex)
- [EN Gene Information Flow](../../bio-ifgt/sections/gene_information_flow.tex)
- [EN Life Attractor](../../bio-ifgt/sections/life_attractor.tex)
- [EN Minimal Developmental Simulation](../../bio-ifgt/sections/minimal_developmental_simulation.tex)
- [self-contained JA manuscript](../../bio-ifgt/main_ja.tex)
- [simulation README](../../bio-ifgt/simulations/minimal_neural_field/README.md)

Working/source-version notes:

- [JA working Formal Mapping](../../bio-ifgt/sections_ja/formal_mapping_ja.md)
- [JA working Core Equations](../../bio-ifgt/sections_ja/core_equations_ja.md)
- [JA working Gene Information Flow](../../bio-ifgt/sections_ja/gene_information_flow_ja.md)
- [JA working Development](../../bio-ifgt/sections_ja/development_morphogenesis_ja.md)
- [JA working Life Attractor](../../bio-ifgt/sections_ja/life_attractor_ja.md)
- [JA working Intelligence](../../bio-ifgt/sections_ja/intelligence_second_attractor_ja.md)

Audit status / traceability:

- [Bio-IFGT audit README](README_ja.md)
- this implementation record

No simulation code, parameter, tracked image, PDF, downstream branch, or upstream VED/IFGT source was changed.

## 5. I identity implementation

Bio continuum \(I(\mathbf r,t)\), toy \(I\), and code array `I` are identified as source-local objects.
The existing nonidentity statement relative to IFGT \(I=f(1-C)\) remains intact.
No carrier, calibration, or observable map was supplied.

## 6. J identity implementation

The continuum vector \(\mathbf J(\mathbf r,t)\) is separated from VED \(J_{ij}\), working-source plain \(J\), and the finite code.
The execution documentation now states that `simulate.py` does not directly integrate an independent `J` array.
This is not a judgment on the formal continuum relation and does not provide the missing aggregation bridge.

## 7. rho / sigma implementation

Both Bio \(\rho\) signatures retain the source-declared progression role and are separated from density uses upstream.
Their exact functional identity is not asserted. Bio \(\sigma\) is described as the source slot of the Bio balance equation;
the gene-event wording, toy \(\sigma_M\), and VED/IFGT \(\sigma\) uses are distinguished without altering any claim disposition outside Phase 01.

## 8. t / tau / step implementation

External equation parameter \(t\), interpretive Bio accumulation \(\tau\), upstream time variables,
and the finite loop step / `DT` are now explicitly distinct. No biological-clock calibration or upstream time map was introduced.

## 9. Phi / F family implementation

The effective potential \(\Phi[I]\), continuum bias vector \(\mathbf F\), threshold response \(F_k\),
and state-space evolution field \(F(x;\theta)\) are distinguished by local signature and domain.
The finite code's lack of directly integrated `Phi` and `J` arrays is documented as an execution fact, not a formal invalidity result.

## 10. G / G_norm / B implementation

The displayed paper quantity \(G=|\nabla I|\) remains unchanged.
Prose now records that the code computes a raw magnitude internally, returns a global normalization used as `G_norm`,
and updates the separate accumulated state `B` from that input. No displayed normalized equation was added.

## 11. S / sigmoid implementation

The symbolic paper \(S(z)\) remains unchanged. Documentation distinguishes it from the current execution helpers:
the general sigmoid uses the existing steepness 8, the eye-specific sigmoid uses 20, and both clip exponential arguments.
These facts do not define a new common function or alter code.

## 12. signature / probability variants

The canonical EN and self-contained JA manuscripts retain the \(\theta\)-bearing threshold and source signatures.
The JA working Markdown retains its omitted-argument forms and now labels them as versioned variants.
Likewise, the canonical conditional probability expression and the working repeated \(P_{\mathrm{life}}\) product both remain unchanged;
the author's intended relation is explicitly OPEN.

## 13. local glyph collisions

The Phase 01 collision ledger COL-01–16 was rechecked. Source prose now supplies local disambiguation where the current reader could
otherwise confuse a sequence length with a field, a nucleotide with a gradient, a state label with an accumulated array,
a coordinate with a state vector, or a response index with a steepness parameter. No global renaming or notation family was adopted.

## 14. equation immutability check

Before editing, displayed equation / align / bracket / double-dollar blocks in all 33 Bio TeX and Markdown sources were hashed.
After editing, all 33 per-file block counts and hashes match exactly. Therefore:

- coefficient, sign, operator, exponent, index, variable, functional form: unchanged;
- displayed equation added / removed: 0 / 0;
- equation semantics changed by formula: NO.

Inline notation appears only in explanatory identity and provenance notes.

## 15. validation

- source-path existence: PASS
- final disposition trace BIO-FD-001–012: 12 / 12
- EN/JA major identity-note parity: PASS
- displayed-math block comparison: PASS, 33 / 33 unchanged
- Markdown fences / display delimiters: PASS
- TeX structural validation: PASS
- temporary EN compile: PASS (`latexmk -pdf`, 29 pages)
- temporary JA compile: PASS (`latexmk -lualatex`, 21 pages; existing font-size substitution warnings only)
- tracked PDFs updated: NO
- relative links in changed Markdown / audit records: PASS
- `git diff --check`: PASS
- temporary/build junk in repository: none introduced

## 16. next phase

Next implementation phase is **Phase 02 — formal equation role / paper-code correspondence**.
It is **NOT STARTED**. This record does not authorize beginning it.
