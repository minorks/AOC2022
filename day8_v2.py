# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:24:12 2022

@author: kyle.minor
"""

from numpy import array
from numpy import amax

def getSubs(tbl,cell):
    return [tbl[cell[0]:cell[0]+1,:cell[1]],   #Left
            tbl[cell[0]:cell[0]+1,cell[1]+1:],   #Right
            tbl[:cell[0],cell[1]:cell[1]+1],   #Up
            tbl[cell[0]+1:,cell[1]:cell[1]+1]]   #Down
    
def checkVis(subs,val):    
    for x in subs:
        if amax(x) < val: return True
    return False  

def getScore(subs,val):
    scores = [0 for x in range(0,4)]
    
    # Left Subscore
    for i in range(0,subs[0].shape[])
    for i in range(0,len(subs[0].values.toList())):
        comp = subs[0].iloc[0,len(subs[0])-(i+1)]
        if comp < val: 
            scores[0] += 1
        else:
            scores[0] += 1
            break
        
    # right Subscore
    for i in range(0,len(subs[1])):
        comp = subs[1].iloc[0,i]
        if comp < val: 
            scores[1] += 1
        else:
            scores[1] += 1
            break
        
    # Up Subscore
    for i in range(0,len(subs[2])):
        comp = subs[2].iloc[len(subs[2])-(i+1),0]
        if comp < val: 
            scores[2] += 1
        else:
            scores[2] += 1
            break
        
    # Up Subscore
    for i in range(0,len(subs[3])):
        comp = subs[3].iloc[i,0]
        if comp < val: 
            scores[3] += 1
        else:
            scores[3] += 1
            break
        
    print (scores)
    return(scores[0]*scores[1]*scores[2]*scores[3])

file = open("C:/Users/kyle.minor/PythonStuff/AOC2022/AOC2022/" \
               "Day8_input.txt")
lines = file.readlines()
for i in range(0,len(lines)):
    lines[i] = list(lines[i].strip())
    for j in range(0,len(lines[i])):
        lines[i][j] = int(lines[i][j])
        
tbl = array(lines)

visCt = 0
score = 0
for i in range(0,tbl.shape[0]):      # By Rows
    for j in range(0,tbl.shape[1]):   # By Columns    
        if (i == 0 or i == tbl.shape[0]-1) or (j == 0 or j == tbl.shape[1]-1):
            visCt += 1
        else:
            subs = getSubs(tbl=tbl,cell=[i,j])
            if checkVis(subs=subs,val=tbl[i,j]):
                visCt += 1
            tScore = getScore(subs=subs,val=tbl[i,j])
            print (tScore)
            if tScore > score:
                score = tScore

print("Part 1: ", visCt)