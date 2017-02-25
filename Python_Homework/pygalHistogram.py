from __future__ import print_function, division
import numpy as nmpy
import pandas as pnd
import pygal as pyg
import os 

data = pnd.read_csv(os.path.join('data','2016-first-quarter-citations.csv'))
data = data.dropna(how='any')

from datetime import datetime
data['DateTime Issued'] = data.apply(lambda row: datetime.strptime(row['Date Issued'] + ':' + row['Time Issued'], '%m/%d/%y:%I:%M %p'), axis=1)

PeoplesAges = data['Cited Person Age']
PeoplesAges = PeoplesAges[PeoplesAges < 100]
listAges = [0]*100

for i in PeoplesAges:
	listAges[int(i)] = listAges[int(i)] + 1

histogram = pyg.Histogram()
labelValues = []

for x in range(0,len(listAges)):
	labelValues.append((listAges[x],x,x+1))

histogram.add('Ages',labelValues)
histogram.render_to_file('solution.svg')
