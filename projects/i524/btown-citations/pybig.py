from __future__ import division, print_function
import numpy as np
import pandas as pd
import pygal as pg
data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')
ages = [int(x) for x in data['Cited Person Age'] if x < 100]
age = list()
min_age = min(ages)
max_age = max(ages)
for x in range(min_age, max_age):
    c = 0
    for y in ages:
        if x == y:
            c = c + 1
    temp = c, x, x + 1
    age.append(temp)
l = pg.Histogram()
l.title = 'Age histogram'
l.add('age', age)
l.render_in_browser()
