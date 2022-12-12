# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:11:17 2022

@author: hokie
"""

file = open("C:\\Users\hokie\\Documents\\Programming\\" \
            "AOC22\\day10_input.txt",'r')
lines = file.readlines()

reg = 1
cycles = dict()

ct = 0
for x in lines:
    ct += 1 # Advance the clock
    cycles[ct] = reg # the next cycle retains the current reg regardless
    struc = x.strip().split(" ")
    if struc[0] == "noop":
        continue
    elif struc[0] == "addx":
        ct += 1 # Advance the clock again
        cycles[ct] = reg
        reg += int(struc[1])
        
checkVals = [20,60,100,140,180,220]
sum = 0
for i in checkVals:
    sum += (i * cycles[i])

print("Part 1: ", sum)

##### Part 2 #####
out = list('' for i in range(0,6))
for i in cycles.keys():
    sCent = cycles[i]
    toPrint = "#" if (i-1)%40 in range(sCent-1,sCent+2) else "."
    
    print("Center: ", sCent,"/n","linePos: ",(i-1)%40)
    out[int((i-1)/40)] += toPrint

for i in out:
    print(i)

