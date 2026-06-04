LATEX := lualatex
BIBTEX := bibtex
MAIN ?= main_ja
BUILD := build
TEXMFVAR := .texmf-var

.PHONY: all pdf ja en clean

all: pdf

ja:
	$(MAKE) pdf MAIN=main_ja

en:
	$(MAKE) pdf MAIN=main

pdf:
	mkdir -p $(BUILD) $(TEXMFVAR)
	TEXMFVAR=$(CURDIR)/$(TEXMFVAR) $(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(MAIN).tex
	if [ -f $(BUILD)/$(MAIN).aux ] && grep -q '\\citation' $(BUILD)/$(MAIN).aux; then cd $(BUILD) && BIBINPUTS=..: $(BIBTEX) $(MAIN); fi
	TEXMFVAR=$(CURDIR)/$(TEXMFVAR) $(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(MAIN).tex
	TEXMFVAR=$(CURDIR)/$(TEXMFVAR) $(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $(MAIN).tex

clean:
	rm -f $(BUILD)/*.aux $(BUILD)/*.bbl $(BUILD)/*.blg $(BUILD)/*.log $(BUILD)/*.out $(BUILD)/*.toc $(BUILD)/*.pdf
