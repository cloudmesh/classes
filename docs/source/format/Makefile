all:
	rm -f *.gz *.zip
	cd simple/latex; make
	cd simple/latex; make clean
	tar cvfz report.tar.gz simple/latex
	zip -r report.zip simple/latex
