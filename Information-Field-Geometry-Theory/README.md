# Information Field Geometry Theory (IFGT)

This repository contains the TeX source for the theoretical framework:

**Information Field Geometry Theory (IFGT)**

---

## Overview

IFGT is a higher-level effective theory that describes informational structures
as geometric configurations.

It is constructed on top of:

- **Vortical Enclosure Dynamics (VED)**  
  A related framework proposing formal constructions and physical
  interpretations from difference, gradient, flow, and enclosure.

IFGT does not replace physical theory.  
Instead, it proposes a **geometric reinterpretation of informational phenomena**
and an OPEN formal correspondence with VED.

---

## Core Idea

- Information is not treated as an abstract symbol or stored object.
- Information is treated as a **persistent geometric structure**.
- Meaning emerges when such structures begin to **constrain information flow**.

---

## Structure

```txt
main.tex     LaTeX entry point
sections/    paper sections included from main.tex
figures/     diagrams and figure source files
refs.bib     bibliography database
ifgt_en.md   English overview draft
ifgt_ja.md   Japanese overview draft
main.pdf     compiled PDF
```

## Current Status

This repository is being prepared as a public source archive for the initial
presentation of IFGT. arXiv identifiers, if assigned, will be added after
submission approval.

The framework is exploratory and should be read as a structural research
proposal rather than a completed physical theory.

## Building

The PDF can be rebuilt with:

```sh
latexmk -pdf main.tex
```

LaTeX build artifacts are ignored by Git. The compiled `main.pdf` is kept in
the repository for convenient reading.

## Relation to VED

IFGT is intended as a companion framework to Vortical Enclosure Dynamics. VED
addresses stabilized quasi-closure as generative physical structure; IFGT
focuses on what it proposes as the residual side of the related process, where
traces of difference persist as informational constraint and observation-like
relations. This is a proposed correspondence: the repository does not supply
explicit translations for the $C$, time, or source-term variables across VED
and IFGT.
In this sense, IFGT treats information not as a separate substance, but as the
residual geometry left by incomplete closure.

## Citation

If you use or discuss this framework before arXiv identifiers are available,
please cite this repository. Formal citation metadata may be added after the
public release structure is finalized.

## License

No explicit license file is currently included. Until a license is added, reuse
permissions should be treated as not yet specified.
