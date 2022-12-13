# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:33:00 2022

@author: hokie
"""

from numpy import sign

file = open("C:\\Users\\hokie\\Documents\\Programming\\AOC22\\" \
            "day12_testInput.txt",'r')
topo = file.readlines()

sCell = [None, None]
eCell = [None, None]
for i in range(0,len(topo)):
    if topo[i].find("S") >= 0:
        sCell[0] = i
        sCell[1] = topo[i].index("S")
    elif topo[i].find("E") >= 0:
        eCell[0] = i
        eCell[1] = topo[i].index("E")
    topo[i] = list(topo[i].strip())
print(sCell,eCell)

def validMoves(cell):
    cellVal = ord(topo[cell[0]][cell[1]])
    if cellVal == ord("S"):
        cellVal = ord("a")
    valid = []
    
    # Left Cell
    if cell[0] > 0 and ord(topo[cell[0]-1][cell[1]]) <= cellVal+1:
        valid.append([-1,0])
    
    # Right Cell
    if cell[0] < len(topo[0])-1 and ord(topo[cell[0]+1][cell[1]]) <= cellVal+1:
        valid.append([1,0])
        
    # Up Cell
    if cell[1] > 0 and ord(topo[cell[0]][cell[1]-1]) <= cellVal+1:
        valid.append([0,-1])
    
    # Down Cell
    if cell[1] < len(topo) and ord(topo[cell[0]][cell[1]+1]) <= cellVal+1:
        valid.append([0,1])
        
    return(valid)

def moveDir(cell):
    return [cell[0]-eCell[0],
            cell[1]-eCell[1]]

# Start at the beginning...
currCell = sCell
ct = 0
while currCell != eCell:
    validMv = validMoves(currCell)
    
    # Prefer to move in the direction of the furthest dimension
    toMove = moveDir(currCell)
    if abs(toMove[0]) > abs(toMove[1]):
        for x in validMv:
            if sign(x[0]) == (-1)*sign(toMove[0]):
                sel = x
                break
    else:
        for x in validMv:
            if sign(x[1]) == (-1)*sign(toMove[1]):
                sel = x
                break
            
    currCell[0] += sel[0]
    currCell[1] += sel[1]
    ct += 1
    
print(ct)
    
    


