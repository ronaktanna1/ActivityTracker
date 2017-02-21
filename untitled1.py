# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:43:27 2017

@author: Ronak"""
import re
import pandas as pd

def pickdata(s):
    point=re.findall('^([0-9][0-9])\n',s)
    p=int(point[0])
    return p
    
datapoint=[]  
a=['34\n\r\w\w','42\n\r\w\w','53\n\r\w\w','21\n\r\w\w']
for i in xrange(0,3):
    datapoint.append(pickdata(a[i]))

print datapoint