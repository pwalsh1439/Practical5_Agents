# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:24:59 2017

@author: Paul
"""
import random


'''
class Agent():
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
  '''

#The Extra work from Pratical  Agents! - Classes and Objects 3
#
class Agent():
    def __init__(self):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
     
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def setx(self, value):
        self._x = value
    def sety(self, value):
        self._y = value  
    x = property(getx, setx, "I'm the 'x' property.")     
    y = property(gety, sety, "I'm the 'y' property.")  
    
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100