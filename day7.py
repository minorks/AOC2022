# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:59:48 2022

@author: kyle.minor
"""

from functools import total_ordering

@total_ordering
class Directory():    
    def __init__(self,superD, name):
        self.name = name
        self.subDirs = []
        self.files = []
        self.superD = superD
        
    def addSub(self, sub):
        if self.subDirs.count(sub) == 0: self.subDirs.append(sub)
        
    def addFile(self, file):
        self.files.append(file)
        
    def getSize(self):
        size = 0        
        for x in self.files:
            size += x.getSize()
        for x in self.subDirs:
            size += x.getSize()
        return size
    
    def __eq__(self,comp):
        return (comp.name == self.name and comp.superD == self.superD)
    
    def __lt__(self,comp):
        return (self.getSize() < comp.getSize())
    
    def __gt__(self,comp):
        return (self.getSize() > comp.getSize())
    
    def __le__(self,comp):
        return (self.getSize() <= comp.getSize())
    
#    def __ge__(self.comp):
#        return (self.getSize() >= comp.getSize())
    
    def __repr__(self):
        return self.name
    
class File():
    def __init__(self,name,size):
        self.name = name
        self.size = size
        
    def getSize(self):
        return self.size

file = open("C:\\Users\\kyle.minor\\PythonStuff\\AOC2022\\" \
            "AOC2022\\day7_input.txt",'r')
lines = file.readlines()

allDirecs = list()
topDirec = Directory(superD=None,name="/")
allDirecs.append(topDirec)

currDirec = topDirec

for ln in lines:
    txt = ln.strip().split(" ")
    if txt[0] == "$":
        if txt[1] == "cd":
            if txt[2] == "/":
                currDirec = topDirec
            elif txt[2] == "..":
                currDirec = currDirec.superD
            else:
                chgDex = currDirec.subDirs.index(\
                            Directory(superD = currDirec, name = txt[2]))
                currDirec = currDirec.subDirs[chgDex]
        elif txt[1] == "ls":
            continue
    elif txt[0] == "dir":
        if currDirec.subDirs.count(Directory( \
                        superD = currDirec,name = txt[1])) == 0:
            new = Directory(superD = currDirec, name = txt[1])
            currDirec.addSub(new)
            allDirecs.append(new)
    else:
        newFile = File(name=txt[1],size=int(txt[0]))
        currDirec.addFile(newFile)
        
lim = 100000
soln = 0
tSize = 0
for x in allDirecs:
    soln += x.getSize() if x.getSize() <= lim else 0
    
print("Part 1: ", soln)

###### Part 2 #######
tSpace = 70000000
dSpace = 30000000

seekSpace = dSpace - (tSpace-allDirecs[0].getSize())
srtDirecs = sorted(allDirecs)

solnDirec = None
for x in srtDirecs:
    if x.getSize() >= seekSpace: 
        solnDirec = x
        break
        
print("Part 2: ",solnDirec.getSize())



        
    

