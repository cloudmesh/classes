FILE=report

UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
OPENCMD=open
endif
ifeq ($(UNAME), Linux)
OPENCMD=xdg-open
endif

all:
	pdflatex ${FILE}
	bibtex ${FILE}
	pdflatex ${FILE}
	pdflatex ${FILE}

real-clean: clean
	rm -rf *.pdf

clean:
	rm -rf *~ *.aux *.bbl *.dvi *.log *.out *.blg *.toc *.fdb_latexmk *.fls *.tdo *.bcf

view:
	$(OPENCMD) ${FILE}.pdf

# all dependce tracking taking care of by Latexmk
fast:
	latexmk -pdf ${FILE}

watch:
	latexmk -pvc -view=pdf ${FILE}

.PHONY: all clean view fast watch
