# Intelligence Part II

## 推論の非閉包性、停止の外部化、創発的停止層

English title: *Non-Closure of Inference, Externalization of Stopping, and Emergent Stopping Layers*

This repository directory contains the scaffold for Intelligence Part II, a Japanese TeX manuscript and an English TeX draft in the VED/IFGT application series.

## Purpose

The purpose of this directory is to organize the Japanese Markdown source draft into an editable LuaLaTeX paper. The manuscript is structured so that the main body and appendices can be edited independently, section by section, while preserving a path toward a future English TeX version.

## Position in the VED Theory Tree

Intelligence Part II follows Intelligence Part I in the intelligence-layer branch of the VED/IFGT application series. Part I formulates intelligence as a non-closed dynamical phenomenon. Part II focuses on the non-closure of inference, the externalization of stopping, and the emergence of stopping layers that stabilize reasoning without closing it absolutely.

Within the broader tree:

- VED supplies the differential-development structure.
- IFGT supplies the field vocabulary of density, flow, potential, and projection.
- Consciousness treats intra-individual temporal non-closure.
- Intelligence Part I treats intelligence as a dynamical phenomenon with local horizon-form.
- Intelligence Part II treats inference and stopping as non-closed structures that require externalized or emergent stopping layers.

## Build

The manuscript assumes LuaLaTeX.

```sh
make ja
make en
```

`make ja` builds `main_ja.tex`; `make en` builds `main.tex`. Both write artifacts to `build/`.

Useful targets:

```sh
make pdf
make ja
make en
make clean
```

## Directory Structure

```text
intelligence-part2/
├── main_ja.tex
├── main.tex
├── preamble_ja.tex
├── preamble.tex
├── refs.bib
├── sections/
│   ├── 00_introduction_ja.tex
│   ├── 01_preliminaries_ja.tex
│   ├── 02_inference_operator_ja.tex
│   ├── 03_nonclosure_theorem_ja.tex
│   ├── 04_response_channels_ja.tex
│   ├── 05_emergent_stopping_layer_ja.tex
│   ├── 06_animism_ja.tex
│   ├── 07_god_ja.tex
│   ├── 08_religion_ja.tex
│   ├── 09_social_blockchain_ja.tex
│   ├── 10_gettier_problem_ja.tex
│   ├── 11_instability_region_ja.tex
│   ├── 12_constructive_clauses_ja.tex
│   └── 13_conclusion_ja.tex
├── appendices/
│   ├── appendix_a_master_table_ja.tex
│   ├── appendix_b_homology_ja.tex
│   ├── appendix_c_part1_mapping_ja.tex
│   ├── appendix_d_optional_notes_ja.tex
│   └── appendix_e_emergence_homology_ja.tex
├── figures/
│   ├── figure_captions.md
│   └── figure_captions_ja.md
├── source_md/
│   ├── intelligence_part2_combined_ja.md
│   ├── intelligence_part2_appendices_ja.md
│   └── intelligence_part2_revision_notes_ja.md
└── build/
```

## Editing Policy

- Keep the Japanese manuscript as the primary source for now.
- Use `_ja.tex` suffixes for Japanese TeX files so future English TeX files can be added cleanly.
- Keep English TeX files without the `_ja` suffix and aligned to the same section boundaries.
- Preserve mathematical notation from the Markdown source when migrating text.
- Move one chapter at a time from `source_md/` into the corresponding `_ja.tex` file in `sections/`.
- Keep appendices separate from the main body and load them only after `\appendix`.
- Avoid local styling beyond `preamble_ja.tex`; keep the TeX easy to revise and translate.
- Future English TeX files should follow the same section boundaries where possible.
- Keep detailed figure captions in `figures/figure_captions_ja.md` and `figures/figure_captions.md`; the LaTeX figure notes are shortened versions.
