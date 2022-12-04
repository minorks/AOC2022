# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:21:05 2022

@author: hokie
"""

def makeRange(txt: str):
    foo = txt.split("-")
    return range(int(foo[0]),int(foo[1])+1)

file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day4_input.txt")
#file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day4_test.txt")
lines = file.readlines()

count = [0,0]
for x in lines:
    pair = x.strip().split(sep=",")
    rgA = makeRange(pair[0])
    rgB = makeRange(pair[1])
    sect = set.intersection(set(rgA), set(rgB))
    if sect == set(rgA) or sect == set(rgB):
        count[0] += 1
    if len(sect) > 0:
        count[1] += 1
    
        
print("Part 1: ",count[0])
print("Part 2: ",count[1])