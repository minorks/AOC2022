# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 07:28:55 2022

@author: hokie
"""

import pandas as pd

def parseLine(txt):
    x = txt.split(" ")
    return [int(x[1]),int(x[3]),int(x[5])]

class Stack():
    
    def __init__(self):
        self.__list = []
        
    def empty(self):
        return len(self.__list) == 0
        
    def push(self,new):
        self.__list.append(new)
        
    def superPush(self,new):
        for x in new:
            self.__list.append(x)
    
    def pop(self):
        return None if self.empty() else self.__list.pop()
    
    def superPop(self,qty):
        if self.empty(): return None
    
        toRet = self.__list[len(self.__list)-qty:]
        
        for i in range(0,qty): 
            self.__list.pop()
        return toRet
    
    def peek(self):
        return None if self.empty() else self.__list[len(self.__list)-1]
    
    def getList(self):
        return self.__list
    
def makeStacks(tbl):
    stacks = []
    for col in tbl.columns:
        myStack = Stack()
        myCol = list(tbl[col])
        myCol.reverse()
        for x in myCol:
            if type(x) == str:
                myStack.push(x)
            else: break
        stacks.append(myStack)
    return stacks
    

file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day5b_input.txt")
lines = file.readlines()

tbl = pd.read_fwf( \
        "C:\\Users\\hokie/Documents/Programming/AOC22/day5a_input.txt", \
        width=3,header=None,skipfooter=1,engine='python')
    
    
stacks_pt1 = makeStacks(tbl)
stacks_pt2 = makeStacks(tbl)
# stacks = []
# for col in tbl.columns:
#     myStack = Stack()
#     myCol = list(tbl[col])
#     myCol.reverse()
#     for x in myCol:
#         if type(x) == str:
#             myStack.push(x)
#         else: break
#     stacks.append(myStack)

for x in lines:
    instr = parseLine(x)
    
    stacks_pt2[instr[2]-1].superPush(stacks_pt2[instr[1]-1].superPop(instr[0]))
    
    for i in range(0,instr[0]):
        stacks_pt1[instr[2]-1].push(stacks_pt1[instr[1]-1].pop())
    
oStr = ["",""]
for x in stacks_pt1:
    oStr[0] += x.peek()[1]
for x in stacks_pt2:
    oStr[1] += x.peek()[1]
          
print("Part 1: ", oStr[0])
print("Part 2: ", oStr[1])

    
    



