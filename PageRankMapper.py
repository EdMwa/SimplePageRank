# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:30:59 2019

@author: JAB
"""

''' mapper of pangerank algorithm'''
import sys
id1 = id2 = None
heros = value = None
count1 = count2 = 0

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 3 and data[1] == 'a':# This is the pangerank value
        count1 += 1
        if count1 >= 2:
          print('%s\t%s' % (id1,0.0))
          
        id1 = data[0]
        value = float(data[2]) 
    else:#This the link relation
      id2 = data[0]
      heros = data[1:]
    if id1 == id2 and id1:
      v = value / len(heros)
      for hero in heros:
          print('%s\t%s' % (hero,v))
      print('%s\t%s' % (id1,0.0))
      id1 = id2 = None
      count1 = 0