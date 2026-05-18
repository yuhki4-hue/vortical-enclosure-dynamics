# conceptual-topography

**Conceptual Topography**  
*A Field-Theoretic Account of Conceptual Landscapes*

VED × IFGT Application Layer 1  
Author: Yuhki Endoh (Independent Researcher)

---

## Overview

This repository contains the LaTeX source for Conceptual Topography,
the first application-layer paper of the VED × IFGT series.

Conceptual Topography applies the field-theoretic structure of IFGT to the emergence of
conceptual landscapes in cognitive and social systems.
All variables conform to the **Master Variable Table v2.1**.

---

## Repository Structure

```
conceptual-topography/
├── main.tex                  # Main document (modular)
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

---

## Series Architecture

| Layer | Theory | Repository |
|-------|--------|------------|
| L0 (generation) | VED Vol. 1–4 | `vortical-enclosure-dynamics/` |
| L0 (structure)  | IFGT          | `IFGT/` |
| L1 (application) | **Conceptual Topography [this]** | `conceptual-topography/` |
| L1 (application) | Consciousness Theory | `[forthcoming]` |
| L1 (application) | Intelligence Theory  | `[forthcoming]` |

---

## Variable Convention

All variables follow the Master Variable Table v2.1 used in the VED × IFGT
series.

Key identities:
- `I = f(1 - C)` — information density from closure degree
- `Φ = K ∗ I` — potential (primary definition; non-local)
- `J_I = -D∇I + μF_I` — information flow (IFGT side)
- `J_C = -D∇C - μαC∇C` — closure flow (VED side)
- `I(x, τ) > 0` — strict positivity; complete closure is not an ordinary
  dynamical state

Bare `J` without subscript is **not used**.

Conceptual-domain uses of these variables are projected or coarse-grained
realizations within a cognitive observation window; they do not redefine the
general IFGT variables.

---

## arXiv Submission

For arXiv submission, use `main_arxiv.tex` (to be generated),
which integrates all sections into a single flat file.

---

## License

Theory documents and figures are released under CC BY 4.0 unless otherwise
noted, following the parent VED repository.
