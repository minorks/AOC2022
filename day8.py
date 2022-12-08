# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 07:33:27 2022

@author: hokie
"""

class Map():
    def __init__(self,data):
        self.tbl = data # Will be a list of text strings
        
    def __cl__(self,dex):
        toChk = self.tbl[:dex[0]]
        for x in toChk:
            if int(x) >= int(self.tbl[dex[0]][dex[1]]): return False
        return True
    
    def __cr__(self,dex):
        toChk = self.tbl[dex[0]:]
        for x in toChk:
            if int(x) >= int(self.tbl[dex[0]][dex[1]]): return False
        return True
    
    def __cu__(self,dex):
        
    

file = open("C:\\Users\\hokie/Documents/Programming/AOC22/day8_input.txt")
lines = file.readlines()


