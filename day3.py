# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:33:29 2022

@author: hokie
"""

def getCommon(txt: str) -> str:
    midDex = int(len(txt)/2)
    aStr = txt[0:midDex]
    bStr = txt[midDex:len(txt)]
    return(list(set.intersection(set(aStr),set(bStr))))

def getCommon3(sacks) -> str:
    return(list(set.intersection(set(sacks[0]),set(sacks[1]),set(sacks[2]))))

def getValue(char: str) -> int:
    asciiVal = ord(char[0])
    capRange = range(ord("A"),ord("Z")+1)
    capTrans = 27 - ord("A")
    
    lcRange = range(ord("a"),ord("z")+1)
    lcTrans = 1 - ord("a")
    
    if asciiVal in capRange:
        return asciiVal + capTrans
    elif asciiVal in lcRange:
        return asciiVal + lcTrans

file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day3_input.txt")
lines = file.readlines()

sum = [0,0]
ct = 0
packs = [None,None,None]
for x in lines:
    sum[0] += getValue(getCommon(x.strip()))
    packs[ct % 3] = x.strip()
    if ct > 0 and ct % 3 == 2:
        sum[1] += getValue(getCommon3(packs))
        packs = [None,None,None]
    ct += 1
    
print("Part 1: ", sum[0])
print("Part 2: ",sum[1])




