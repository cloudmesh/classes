change:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > CHANGELOG
