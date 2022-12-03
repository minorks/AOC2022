# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:55:08 2022

@author: kyle.minor
"""

import pandas as pd

file = open("C:\\Users\\kyle.minor\\PythonStuff\\AOC2022\\day1_input.txt",'r')
lines = file.readlines()

elves = []

sum = 0
for x in lines:
    if len(x.strip()) == 0:
        elves.append(sum)
        sum = 0
    else:
        sum += int(x)
        
elves.sort()
print(elves[len(elves)-1])

print(elves[len(elves)-1]+elves[len(elves)-2]+elves[len(elves)-3])