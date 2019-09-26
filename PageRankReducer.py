# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:31:57 2019

@author: JAB
"""

''' reducer of pagerank algorithm'''
import sys
last = None
values = 0.0
alpha = 0.8
N = 4# Size of the web pages
for line in sys.stdin:
    data = line.strip().split('\t')
    hero,value = data[0],float(data[1])
    if data[0] != last:
        if last:
            values = alpha * values + (1 - alpha) / N
            print('%s\ta\t%s' % (last,values))
        last = data[0]
        values = value
    else:
        values += value #accumulate the page rank value
if last:
    values = alpha * values + (1 - alpha) / N
    print('%s\ta\t%s' % (last,values))