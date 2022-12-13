# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 09:13:56 2022

@author: hokie
"""

import time

class Monkey():
    
    def __init__(self,xid,items,op,testDiv,testRes):
        self.id = xid
        self.items = list(items)
        self.op = op
        self.testDiv = testDiv
        self.testRes = testRes
        self.counter = dict()
        
    def catch(self,item):
        self.items.append(item)
        
    def inspect(self,item,reliefDiv,maxMod):
        old = self.items[0]
        
        # Counter for item inspection
        if self.counter.get(item) == None:
            self.counter[item] = 1
        else:
            self.counter[item] += 1
            
        # Action to change item upon inspection
        toAdd = old if self.op[2] == "old" else int(self.op[2])
        new = (old + toAdd) if self.op[1] == "+" else (old * toAdd)
            
        # Relief factor application
        if reliefDiv > 1:
            new = int(new / reliefDiv)
            
        new = new % maxMod
        
        # Return monkey to throw to AND new item factor
        self.items.remove(item)
        return [self.testRes[new % self.testDiv == 0],new]
    
    def getCount(self, item = None):
        if item == None:
            toRet = 0
            for i in self.counter.keys():
                toRet += self.counter[i]
        else:
            toRet = self.counter[item]
        return toRet
    
class Parser():
    def __init__(self,file):
        lines = file.readlines()
        self.monkeys = self.parseFile(lines)
            
    def parseFile(self,lines):
        monkeys = dict()
        
        resLst = dict()
        for x in lines:    
            line = x.strip().split(" ")
            if line[0].find("Monkey") >= 0:
                xid = self.__newMky(line)
            elif line[0].find("Starting") >= 0:
                items = list(self.__newItems(line))
            elif line[0].find("Operation") >= 0:
                op = self.__newOp(line)
            elif line[0].find("Test") >= 0:
                testDiv = self.__newTest(line)
            elif line[0].find("If") >= 0:
                newRes = self.__newRes(line)
                resLst[newRes[0]] = newRes[1]
            else:
                monkeys[xid] = Monkey(xid,items,op,testDiv,resLst)
                resLst = dict()
        monkeys[xid] = Monkey(xid,items,op,testDiv,resLst)
        return monkeys
        
    def __newMky(self,line):
        return int(line[1].split(":")[0])

    def __newItems(self,line):
        aLine = line[2:]
        toRet = list()
        for i in range(0,len(aLine)):
            toRet.append(int(aLine[i].split(",")[0]))
        return toRet
    
    def __newOp(self,line):
        return line[3:6]
    
    def __newTest(self,line):
        return int(line[len(line)-1])
    
    def __newRes(self,line):
        return [True if line[1].find("true") >= 0 else False,int(line[5])]

def mim(file,rounds=20,relief=3,part=1):  
    
    file = open(file)
    monkeys = Parser(file).monkeys
    
    mod = 1
    for x in monkeys.keys():
        mod *= monkeys[x].testDiv
    
    for ct in range(0,rounds):
        for mk in monkeys.keys():
            myMk = monkeys[mk]
            for i in range(0,len(myMk.items)):
                item = myMk.items[0]
                toMky = myMk.inspect(item=item,reliefDiv=relief,maxMod=mod)
                monkeys[toMky[0]].catch(toMky[1])
                
    top = None
    bot = None
    for i in monkeys.keys():
        if top == None: 
            top = monkeys[i]
        elif bot == None:
            if top.getCount() >= monkeys[i].getCount():
                bot = monkeys[i]
            else:
                bot = top
                top = monkeys[i]
        else:
            topCt = top.getCount()
            botCt = bot.getCount()
            if monkeys[i].getCount() > topCt:
                bot = top
                top = monkeys[i]
            elif monkeys[i].getCount() > botCt:
                bot = monkeys[i]
        if top != None and bot != None:
            print("Top :", top.id, top.getCount(), \
                  " Bottom: ", bot.id, bot.getCount())
    
    mb = top.getCount() * bot.getCount()

    print("Part ", part,": ", mb)
    
# file = open("C:\\Users\hokie\\Documents\\Programming\\" \
#             "AOC22\\day11_input.txt",'r')
# file = open("C:\\Users\\kyle.minor\\PythonStuff\\AOC2022\\AOC2022\\" \
#             "day11_testInput.txt",'r')

mim(file= "C:\\Users\hokie\\Documents\\Programming\\" \
            "AOC22\\day11_input.txt")


mim(file ="C:\\Users\hokie\\Documents\\Programming\\" \
            "AOC22\\day11_input.txt", rounds=10000,relief=1,part=2)
    
    
# 12727678864 too low for part 2

        
    
        