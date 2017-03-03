UNAME := $(shell uname)
GIT_RECENT_TAG := $(shell git describe --abbrev=0 --tags)

BROWSER=firefox
ifeq ($(UNAME), Darwin)
BROWSER=open
endif
ifeq ($(UNAME), Linux)
BROWSER=xdg-open
endif
ifeq ($(UNAME), Windows)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif
ifeq ($(UNAME), CYGWIN_NT-6.3)
BROWSER=/cygdrive/c/Program\ Files\ \(x86\)/Google/Chrome/Application/chrome.exe
endif

doc: 
	cd docs; make html

all: doc pdf
	echo done

notebooks:
	cd  docs/source/notebooks/; jupyter nbconvert --to rst facedetection.ipynb

pdf: 
	cd docs;  make latex 
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes 
	# cd docs/build/latex; bibtex Classes
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes 
	cp docs/build/latex/i524-notes.pdf docs/build/html

bview:
	$(BROWSER) docs/build/html/i524-notes.pdf

b: 
	cd docs;  make latex
	cp -r docs/book-template/* docs/build/latex
	perl -ne 'print unless 1../begin{document}/' < docs/build/latex/i524-notes.tex > /tmp/content.tex
	sed '/end{document}/ {$!N;d;}' /tmp/content.tex > docs/build/latex/content.tex
	#cd docs/build/latex; pdflatex book
	cd docs/build/latex; pdflatex -interaction  nonstopmode  book
	# cd docs/build/latex; biber book
	cd docs/build/latex; pdflatex -interaction  nonstopmode  book
	cd docs/build/latex; pdflatex -interaction  nonstopmode  book
	cp docs/build/latex/book.pdf docs/build/html


pdfview:
	$(BROWSER) docs/build/latex/book.pdf

watch:
	watchmedo shell-command --patterns="Makefile;*.rst;*.csv;*.py" --recursive --command='make doc'

build: clean
	touch docs/source/index.rst

bpublish: publish
	cp docs/build/latex/book.pdf docs/build/html

publish:
	ghp-import -n -p docs/build/html

view:
	$(BROWSER) docs/build/html/index.html

log:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > docs/source/changelog.rst
	git commit -m "chg: dev: Update changelog" docs/source/changelog.rst
	git push

notes:
	make clean
	rm -rf /tmp/notes-i524
	mkdir -p /tmp/notes-i524
	cp -r . /tmp/notes-i524
	cp /tmp/notes-i524/docs/source/notes.rst /tmp/notes-i524/docs/source/index.rst
	cd /tmp/notes-i524; echo "R" | make pdf || true
	cp /tmp/notes-i524/docs/build/latex/Classes.pdf .


# FIXME: should be cloudmesh/classes
dockerimage: Dockerfile $(wildcard docker/*)
	for tag in latest $(GIT_RECENT_TAG); do \
	  time docker build -t badi/cloudmesh_classes:$(GIT_RECENT_TAG) . ;\
	done

# FIXME this should be cloudmesh/classes
dockerpublish: dockerimage
	for tag in latest $(GIT_RECENT_TAG); do \
	  time docker push badi/cloudmesh_classes:$(GIT_RECENT_TAG) ; \
	done

dockerrun: dockerimage
	time docker run \
	  -e HOST_UID=$(shell id -u) \
	  -e HOST_GID=$(shell id -g) \
	  -v $(shell pwd):/data \
	  -it \
	  --rm \
	  badi/cloudmesh_classes:latest \
	  make all

######################################################################
# CLEANING
######################################################################

clean:
	rm -rf *.zip
	rm -rf *.egg-info
	rm -rf *.eggs
	rm -rf docs/build
	rm -rf build
	rm -rf dist
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete
	rm -rf .tox
	rm -f *.whl

######################################################################
# TAGGING
######################################################################

tag:
	bin/new_version.sh

rmtag:
	python setup.py rmtag

