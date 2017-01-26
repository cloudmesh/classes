UNAME := $(shell uname)

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

pdf: 
	cd docs;  make latex 
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes 
	# cd docs/build/latex; bibtex Classes
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes
	cd docs/build/latex; pdflatex -interaction  nonstopmode  i524-notes 
	cp docs/build/latex/i524-notes.pdf docs/build/html

pdfview:
	$(BROWSER) docs/build/html/i524-notes.pdf

watch:
	watchmedo shell-command --patterns="Makefile;*.rst;*.csv;*.py" --recursive --command='make doc'

build: clean
	touch docs/source/index.rst

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

