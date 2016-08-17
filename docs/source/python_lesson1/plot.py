from __future__ import print_function

import matplotlib.pyplot as plt

import pandas as pd

import sqlite3
import sys


if __name__ == '__main__':

    dbfile = sys.argv[1]

    conn = sqlite3.connect(dbfile)
    results = pd.read_sql('SELECT * from bozorth3 ORDER BY score DESC', con=conn)

    plt.hist(results.score, log=True)
    plt.xlabel('Score')
    plt.ylabel('Count')
    plt.show()
