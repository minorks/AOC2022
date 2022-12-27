# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:08:08 2022

@author: hokie
"""

class Runner():
    def __init__(self,fName):
        self.fName = fName
        
    def reset(self):
        file = open(self.fName)
        self.orig = file.readlines()
        self.monkeys = dict()
        self.wait = dict()
        
    def doPart1(self):
        self.reset()
        for i in range(0,len(self.orig)):
            ln = self.orig[i].strip().split(" ")
            
            self.processLine(ln)
            
        print("Part 1:",self.monkeys["root"])
        
    def processLine(self,ln,part=1):
        mky = ln[0].split(":")[0]
        
        if part == 2 and mky == "humn":
            ln[1] = "x"
            return
        
        if len(ln) == 2:
            self.addToDict(mky,int(ln[1]))
        elif self.monkeys.get(ln[1]) is not None and self.monkeys.get(ln[3]) is not None:
            self.doOp(mky,self.monkeys[ln[1]],self.monkeys[ln[3]],ln[2])
        else:
            self.wait[mky] = [ln[1] if self.monkeys.get(ln[1]) == None else self.monkeys[ln[1]], \
                         ln[2], \
                         ln[3] if self.monkeys.get(ln[3]) == None else self.monkeys[ln[3]]]
                
        for x in self.wait:
            if isinstance(self.wait[x][0],int) and isinstance(self.wait[x][2],int):
                self.doOp(x,self.wait[x][0],self.wait[x][2],self.wait[x][1])
        
        
        
    def doPart2(self):
        self.reset()
        
        for i in range(0,len(self.orig)):
            ln = self.orig[i].strip().split(" ")
            self.processLine(ln,part=2)
            
        tgt = self.wait['root'][0] if \
            isinstance(self.wait['root'][0],int) else \
                self.wait['root'][2]
        oth =  self.wait['root'][0] if \
            not isinstance(self.wait['root'][0],int) else \
                self.wait['root'][2]      
        
        foo = self.solver(tgt,oth)
        print("Part 2:", foo)
        
    def solver(self,tgt,oth):
        if oth != 'humn':
            rcd = self.wait[oth] if self.wait.get(oth) is not None \
                else self.monkeys[oth]
            if isinstance(rcd[0],int):
                if rcd[1] == "+": tgt -= rcd[0]
                elif rcd[1] == "-": tgt = rcd[0] - tgt
                elif rcd[1] == "*": tgt = int(tgt / rcd[0])
                else: tgt = int(rcd[0] / tgt)
                return self.solver(tgt,rcd[2])
            elif isinstance(rcd[2],int):
                if rcd[1] == "+": tgt -= rcd[2]
                elif rcd[1] == "-": tgt += rcd[2]
                elif rcd[1] == "*": tgt = int(tgt / rcd[2])
                else: tgt *= rcd[2]
                return self.solver(tgt,rcd[0])
        else:
            return tgt
        
    def doOp(self,mky,valA,valB,op):
        if op == "+":
            self.addToDict(mky,valA + valB)
        elif op == "-":
            self.addToDict(mky,valA - valB)
        elif op == "*":
            self.addToDict(mky,valA * valB)
        elif op == "/":
            self.addToDict(mky,int(valA / valB))

    def addToDict(self,mky,val):
        self.monkeys[mky] = val
        
        toAct = set()
        for x in self.wait:
            if self.wait[x][0] == mky:
                self.wait[x][0] = val
            elif self.wait[x][2] == mky:
                self.wait[x][2] = val
            
            if isinstance(self.wait[x][0],int) and isinstance(self.wait[x][2],int):
                toAct.add(x)
                
        for x in toAct:
            info = self.wait[x]
            self.wait.pop(x)
            self.doOp(x,info[0],info[2],info[1])

runner = Runner(fName = "C:\\Users\\hokie\\Documents\\Programming\\AOC22\\" \
            "day21_input.txt")
runner.doPart1()
runner.doPart2()
# 9443921358293 too high

########################
    