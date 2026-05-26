# Intelligence Part I

This directory contains the LaTeX source for *Structural Constraints on Intelligence as a Dynamical Phenomenon*, the first paper in the intelligence layer of the VED / IFGT application series.

The Japanese source is generated from the working manuscript `draft_ja.md` and organized into modular TeX sections under `sections/`, with `_ja` suffixes reserved for Japanese files.

Figures 1--5 are included under `figures/`. The LaTeX manuscript uses the PNG versions for compilation, while the SVG files are preserved as editable source figures.

## Build

Use LuaLaTeX because the manuscript is Japanese:

```sh
lualatex main_ja.tex
bibtex main_ja
lualatex main_ja.tex
lualatex main_ja.tex
```
