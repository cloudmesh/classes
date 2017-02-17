"""Usage: python find_repos.py [-h] RAW_LOG_FILE

List all repos from which pull requests were generated from and the
datetime of the last pull request.

Arguments:
  RAW_LOG_FILE  A file containing the output of 'git log --raw'

Options:
  -h --help

"""
from __future__ import print_function, division
import os, re
from docopt import docopt
from dateutil import parser

P = r'Merge pull request #\d+ from (.+/.+)'


if __name__ == '__main__':
	args = docopt(__doc__)

	if not os.path.exists(args['RAW_LOG_FILE']):
		raise ValueError('Path does not exist: %s' % args['RAW_LOG_FILE'])

	repos = {}	
	curr_date = None
	with open(args['RAW_LOG_FILE'], 'r') as f:
		for line in f:
			if line.startswith('Date:'):
				curr_date = parser.parse(line[5:].strip())
			else:
				m = re.search(P, line)
				if m is not None:
					repo = m.group(1)
					if repo not in repos:
						repos[repo] = curr_date
					else:
						if curr_date > repos[repo]:
							repos[repo] = curr_date

	for repo, last_pr in repos.items():
		print(repo, last_pr)
