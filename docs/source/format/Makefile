all:
	rm -f *.gz *.zip
	cd report/latex; make
	cd report/latex; make clean
	tar cvfz report.tar.gz report
	zip -r report.zip report
