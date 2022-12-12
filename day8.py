# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 07:33:27 2022

@author: hokie
"""
from pandas import read_fwf

def getSubs(tbl,cell):
    return [tbl.iloc[cell[0]:cell[0]+1,:cell[1]],   #Left
            tbl.iloc[cell[0]:cell[0]+1,cell[1]+1:],   #Right
            tbl.iloc[:cell[0],cell[1]:cell[1]+1],   #Up
            tbl.iloc[cell[0]+1:,cell[1]:cell[1]+1]]   #Down

def checkVis(tbl,cell):    
    subs = getSubs(tbl,cell)
    val = tbl.iloc[cell[0],cell[1]]
    
    for x in subs:
        if max(x.max()) < val: return True
    
    return False  

def getScore(tbl,cell):
    subs = getSubs(tbl,cell)
    scores = [0 for x in range(0,4)]
    val = tbl.iloc[cell[0],cell[1]]
    
    # Left Subscore
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
    
        

#file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day8_input.txt")
file = open("C:/Users/kyle.minor/PythonStuff/AOC2022/AOC2022/" \
               "Day8_testInput.txt")
cols = len(file.readline().strip())

tbl = read_fwf("C:/Users/kyle.minor/PythonStuff/AOC2022/AOC2022/" \
               "Day8_testInput.txt",widths=[1 for x in range(0,cols)], \
               header=None)

visCt = 0
score = 0
for i in range(0,len(tbl)):      # By Rows
    for j in range(0,len(tbl.columns)):   # By Columns    
        if (i == 0 or i == len(tbl)-1) or (j == 0 or j == len(tbl.columns)-1):
            visCt += 1
        else:
            if checkVis(tbl=tbl,cell=[i,j]):
                visCt += 1
            tScore = getScore(tbl,cell=[i,j])
            print (tScore)
            if tScore > score:
                score = tScore

print("Part 1: ", visCt)
print("Part 2: ", tScore)




