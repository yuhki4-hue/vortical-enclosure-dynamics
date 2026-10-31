# conceptual-topography

**Conceptual Topography**  
*A Field-Theoretic Account of Conceptual Landscapes*

VED × IFGT Application Layer 1  
Author: Yuhki Endoh (Independent Researcher)

---

## Overview

This repository contains the LaTeX source for Conceptual Topography,
the first application-layer paper of the VED × IFGT series.

Conceptual Topography proposes model-local cognitive and social interpretations
of IFGT's field-theoretic vocabulary. Definitions, qualitative hypotheses, and
cross-scale comparisons are distinguished from established mechanisms or
validated mappings. The intended notation continuity attributed to the
**Master Variable Table v2.1** is retained; the exact artifact/version and
typed inheritance remain unresolved.

## Source Authority and Revision Status

The content authority is the canonical EN source, `main.tex` and its 12
included sections. The authorized Japanese translation counterpart is
`main_ja.tex` with 12 parallel `sections_ja/*_ja.tex` files.
`conceptual_topography_ja.md` is retained unchanged as a WORKING / historical
reference, not as the content authority for either canonical version.

The closed audit freezes revision dispositions, not theory validation.
The independent post-implementation consistency audit is COMPLETE:
PASS WITH ADVISORIES; CT core/source revision is CLOSED WITH ADVISORIES.
The global equation-change requirement remains OPEN, with no equation change
implemented and 22 research OPEN families preserved.

Distributions: [EN PDF](main.pdf), 22 pages, FRESH WITH ADVISORIES;
JA PDF（公開版未収録: `main_ja.pdf`）, 23 pages, FRESH WITH ADVISORIES. The Japanese translation
preserves current EN scope and mathematics and reuses the three figure assets.
Both PDFs have been visually inspected; freshness is not validation.

See the [frozen audit](../notes/ct_audit/07_final_audit_and_frozen_dispositions_v1.0_ja.md),
the [independent consistency audit](../notes/ct_audit/implementation/05_independent_post_implementation_consistency_audit_v1.0_ja.md),
and the [Japanese translation/distribution record](../notes/ct_audit/implementation/06_japanese_canonical_tex_and_distribution_v1.0_ja.md).

---

## Repository Structure

```
conceptual-topography/
├── main.tex                  # Canonical EN content authority
├── main_ja.tex               # Authorized Japanese translation
├── sections_ja/              # 12 parallel *_ja.tex sections
├── main.pdf / main_ja.pdf    # EN / JA distributions
├── conceptual_topography_ja.md # WORKING historical reference
├── refs.bib                  # Bibliography
├── sections/
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── intuitive_picture.tex
│   ├── formal_mapping.tex
│   ├── core_equations.tex
│   ├── structural_interpretation.tex
│   ├── dynamics.tex
│   ├── multiscale.tex
│   ├── pathologies.tex
│   ├── relation_to_note.tex
│   ├── discussion.tex
│   └── conclusion.tex
└── figures/                  # Figure assets
```

---

## Build

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or with latexmk:

```bash
latexmk -pdf main.tex
```

Japanese translation (repository-standard LuaLaTeX / LuaTeX-ja setup,
`ltjsarticle`, existing TeX Japanese fonts):

```bash
latexmk -lualatex -interaction=nonstopmode -halt-on-error main_ja.tex
```

EN and JA use separate job names and share `refs.bib` and `figures/`.

---

## Series Architecture

| Layer | Theory | Repository |
|-------|--------|------------|
| L0 (generation) | VED Vol. 1–4 | `vortical-enclosure-dynamics/` |
| L0 (structure)  | IFGT          | `Information-Field-Geometry-Theory/` |
| L1 (application) | **Conceptual Topography [this]** | `conceptual-topography/` |
| L1 (application) | Consciousness Theory | [current repository source](../consciousness/main.tex) |
| L1 (application) | Intelligence Theory | [Part I](../intelligence-part1/README.md), [Part II](../intelligence-part2/README.md) |

---

## Variable Convention

The notation records an intended relationship to the Master Variable Table
v2.1, whose exact source/version remains unresolved. Matching notation or
formula shape does not establish a shared quantity or typed derivation.

Existing relations and conventions (formal status unchanged):

- `I = f(1 - C)` — general IFGT information density; CT uses its
  cognitive-window projection
- `Φ = K ∗ I` — potential (primary definition; non-local)
- `J_I = -D∇I + μF_I` — information flow (IFGT side)
- `J_C = -D∇C - μαC∇C` — closure flow (VED side)
- `I(x, τ) > 0` — strict positivity; complete closure is not an ordinary
  dynamical state

Bare `J` without subscript is **not used**.

Conceptual-domain uses are proposed projected or coarse-grained interpretations
within a cognitive observation window, without redefining general IFGT variables.
The series table is navigation and explanatory positioning, not proof or
generation order. Current Consciousness/Intelligence sources do not establish
the identity of the older companion note or validate CT.
The exact note artifact and its version relation remain unresolved.

Figure 3 now uses `J_I` for the local CT flow label. The diagram remains a
proposed feedback schematic, not a causal proof or executed dynamics.

---

## arXiv Submission

For arXiv submission, a flattened `main_arxiv.tex` can be generated from the
modular source.

---

## License

Theory documents and figures are released under CC BY 4.0 unless otherwise
noted, following the parent VED repository.
