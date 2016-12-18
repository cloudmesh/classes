from __future__ import print_function

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import sqlite3
import sys


def mk_short_labels(series, start=7):
    for size in xrange(start, len(series[0])):
        if len(series) == len(set(map(lambda s: s[:size], series))):
            break

    short = map(lambda s: s[:size], series)
    return short

if __name__ == '__main__':

    dbfile = sys.argv[1]
    nprobes = int(sys.argv[2])

    conn = sqlite3.connect(dbfile)

    df = pd.read_sql("SELECT probe from bozorth3 ORDER BY score LIMIT '%s'" % nprobes,
                     con=conn)


    shortlabels = mk_short_labels(df.probe)

    plt.figure()

    for i, probe in df.probe.iteritems():
        stmt = "SELECT gallery, score FROM bozorth3 WHERE probe = ? ORDER BY gallery DESC"
        matches = pd.read_sql(stmt, params=(probe,), con=conn)
        xs = np.arange(len(matches))
        plt.plot(xs, matches.score, label='probe %s' % shortlabels[i])

    plt.legend()
    plt.show()

    # plt.hist(results.score, log=True)
    # plt.xlabel('Score')
    # plt.ylabel('Count')
    # plt.grid()
    # plt.show()
