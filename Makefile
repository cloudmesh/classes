all:
	cd docs; make html

change:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > CHANGELOG
