# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:52:17 2022

@author: kyle.minor
"""

def getResult(op: str,me :str) -> str:
        if op == "A":
            if me == "X": return("Draw")
            elif me == "Y": return("Win")
            elif me == "Z": return("Lose")
        elif op == "B":
            if me == "X": return("Lose")
            elif me == "Y": return("Draw")
            elif me == "Z": return("Win")
        elif op == "C":
            if me == "X": return("Win")
            elif me == "Y": return("Lose")
            elif me == "Z": return("Draw")
            
def pt2Result(op: str,res :str) -> str:
        if op == "A": #Rock
            if res == "X": return("Z") #Scissors = Lose
            elif res == "Y": return("X") #Rock = Draw
            elif res == "Z": return("Y") #Paper = Win
        elif op == "B": #Paper
            if res == "X": return("X")
            elif res == "Y": return("Y")
            elif res == "Z": return("Z")
        elif op == "C": #Scissors
            if res == "X": return("Y")
            elif res == "Y": return("Z")
            elif res == "Z": return("X")

file = open("C:\\Users\\kyle.minor\\PythonStuff\\AOC2022\\day2_input.txt",'r')
lines = file.readlines()

opVals = {"A" : 1,
          "B" : 2,
          "C" : 3}

myVals = {"X" : 1,
          "Y" : 2,
          "Z" : 3}

scores1 = {"Win" : 6,
          "Draw" : 3,
          "Lose" : 0}

scores2 = {"Z" : 6,
          "Y" : 3,
          "X" : 0}

tot1 = 0
tot2 = 0
for x in lines:
    ln = x.strip().split(" ")
    res1 = getResult(ln[0],ln[1])
    res2 = pt2Result(ln[0],ln[1])
    tot1 += myVals.get(ln[1])+scores1.get(res1)
    tot2 += myVals.get(res2)+scores2.get(ln[1])
    
print("Part 1:", tot1)
print("Part 2:", tot2)