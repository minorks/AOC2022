# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:31:42 2022

@author: hokie
"""

import pandas as pd

tbl = pd.read_csv("~/Documents/Programming/cy21_day1",header=None)
ct = 0

for i in range(1,len(tbl)):
    ct += 1 if tbl.iat[i-1,0] < tbl.iat[i,0] else 0
    
print(ct)

ct = 0
for i in range(3,len(tbl)):
    subA = tbl.iat[i-3,0] + tbl.iat[i-2,0] + tbl.iat[i-1,0]
    subB = tbl.iat[i-2,0] + tbl.iat[i-1,0] + tbl.iat[i,0]
    ct += 1 if subA < subB else 0
    
print(ct)
    