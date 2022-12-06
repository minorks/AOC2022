# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:11:37 2022

@author: kyle.minor
"""

def isToken(txt: str) -> bool:
    for i in range(0,len(txt)):
        if txt.count(txt[i]) > 1: return False
    return True

txt = open("C:\\Users\\kyle.minor\\PythonStuff\\AOC2022" \
                "\\AOC2022\\day6_input.txt").read()
#txt = "bvwbjplbgvbhsrlpgdmjqwftvncz"

ans = [0,0]

ct = [3,3]
isDone = [False,False]
for i in range(4,len(txt)):
    ct[0] += 1
    ct[1] += 1
    if isToken(txt[i-4:i]) and not isDone[0]: 
        ans[0] = ct[0]
        isDone[0] = True
        
    if i >= 14 and isToken(txt[i-14:i]) and not isDone[1]:
        ans[1] = ct[1]
        isDone[1] = True
        break

print("Part 1: ", ans[0])
print("Part 2: ", ans[1])


