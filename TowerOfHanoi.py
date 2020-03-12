
import sys

import PySide2
from PySide2.QtCore import *
from PySide2.QtWidgets import  *
from PySide2.QtGui import *
import turtle as t

class Disk(object):
    def __init__(self,name,x,y,h,w,color):
        self.name = name
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.color = color
    
    def newpos(self,x,y):
        self.x = x
        self.y = y

    def cleardisk(self):
        t.seth(0)
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.forward(self.w/2)
        t.right(90)
        t.forward(self.h)
        t.right(90)
        t.forward(self.h)
        t.right(90)
        t.forward(self.h)
        t.right(90)
        t.forward(self.w/2)
        t.end_fill()
        t.pencolor("black")

class Pole(object):
    def __init__(self,name,stack,toppos,x,y,thickness,length,color)

    
