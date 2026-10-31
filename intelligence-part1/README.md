# Intelligence Part I

This directory contains the LaTeX source for *Structural Constraints on Intelligence as a Dynamical Phenomenon*, the first paper in the intelligence layer of the VED / IFGT application series.

The Japanese working manuscript is retained in `draft_ja.md`; the current distributed build authority is `main_ja.tex` together with the modular files under `sections_ja/`. Cross-domain Bio-IFGT wording in the working manuscript is historical context, while the current TeX/PDF uses the scoped proposed-comparison wording.

Figures 1--5 are included under `figures/`. The LaTeX manuscript uses the PNG versions for compilation, while the SVG files are preserved as editable source figures.

## Build

Use LuaLaTeX because the manuscript is Japanese:

```sh
lualatex main_ja.tex
bibtex main_ja
lualatex main_ja.tex
lualatex main_ja.tex
```
