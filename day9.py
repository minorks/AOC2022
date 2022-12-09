# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:10:40 2022

@author: kyle.minor
"""

def checkPos(headCell,tailCell):
    if (tailCell[0] <= headCell[0]+1 and tailCell[0] >= headCell[0]-1) and \
        (tailCell[1] <= headCell[1]+1 and tailCell[1] >= headCell[1]-1):
            return True
    return False

def moveTail(headCell,tailCell):
    toMove = [0,0]
    
    if tailCell[0] == headCell[0] and tailCell[1] != headCell[1]:
        toMove[0] == 0
        toMove[1] = 1 if tailCell[1] < headCell[1] - 1 else -1
    elif tailCell[0] != headCell[0] and tailCell[1] == headCell[1]:
        toMove[1] == 0
        toMove[0] = 1 if tailCell[0] < headCell[0] - 1 else -1
    else:
        toMove[0] = 1 if headCell[0]-tailCell[0] >= 1 else -1
        toMove[1] = 1 if headCell[1]-tailCell[1] >= 1 else -1
    return toMove     

def swingRope(knots=2):
#    file = open("C:/Users/kyle.minor/PythonStuff/" \
#                "AOC2022/AOC2022/day9_testInput.txt")
    file = open("C:/Users/kyle.minor/PythonStuff/" \
                    "AOC2022/AOC2022/day9_input.txt")
    
    myKnots = list()
    for i in range(0,knots):
        myKnots.append([0,0])
        
    #headCell = myKnots[0]
    #tailCell = myKnots[len(myKnots)-1]

    visited = set()
    
    while True:
        line = file.readline()
        if (line == ""): 
            break
        hMove = list(line.strip().split(sep=" "))
    
        if hMove[0] == "U" or hMove[0] == "D":
            mDex = 0
            mDir = -1 if hMove[0] == "U" else 1
        elif hMove[0] == "R" or hMove[0] == "L":
            mDex = 1
            mDir = -1 if hMove[0] == "L" else 1
            
        for i in range(0,int(hMove[1])):
            myKnots[0][mDex] += mDir   # Move the actual head
            head = myKnots[0]
            
            for k in range(1,len(myKnots)):
                follow = myKnots[k]
                if not checkPos(head,follow):
                    toMove = moveTail(head,follow)
                    for j in range(0,len(toMove)):
                        myKnots[k][j] += toMove[j]
                head = myKnots[k]        
                
            visited.add(tuple(myKnots[len(myKnots)-1]))
                
    return(visited)    


print("Part 1: ", len(swingRope(knots=2)))
print("Part 2: ", len(swingRope(knots=10)))

            
            
            
    

    

    
    





