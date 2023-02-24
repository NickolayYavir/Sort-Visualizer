import numpy as np
from tkinter import Canvas

from config import *


class Element:
    
    def __init__(self,canvas:Canvas,posX1:int,posY1:int,posX2:int,value:int,color="white"):
        self.value = value
        self.posX1 = posX1
        self.posY1 = posY1
        self.posX2 = posX2
        self.color = color
        self.canvas = canvas
        self.id = canvas.create_rectangle(self.posX1, self.posY1, self.posX2, self.value, fill=self.color) 

    def swapElementValue(el1, el2):
        temp = el1.get_value()
        el1.canvas.coords(el1.id, el1.posX1, el1.posY1, el1.posX2, el2.get_value())
        el2.canvas.coords(el2.id, el2.posX1, el2.posY1, el2.posX2, temp)
        el1.set_value(el2.get_value())
        el2.set_value(temp)

    def get_value(self):
        return self.value
    
    def set_value(self, value:int):
        self.value = value

    def set_color(self, color:str):
        self.color = color
        self.canvas.itemconfig(self.id, fill=color)


class ElementsManager:
    
    def __init__(self, canvas:Canvas):
        self.canvas = canvas
        self.createElements()

    def createElements(self):
        self.canvas.delete("all")
        self.arr = []
        posX1 = 0
        posY1 = WINDOW_HEIGHT * 0.65

        for i in range(SORTING_ELEMENT_AMOUT):
            posX2 = posX1 + ELEMENT_WIDTH
            posY2 = posY1 - np.random.randint(1, WINDOW_HEIGHT * 0.65)
            self.arr.append(Element(self.canvas, posX1, posY1, posX2, posY2, 'white'))
            posX1 += ELEMENT_WIDTH

    def __paint_sorted(self, color):
        for i in range(SORTING_ELEMENT_AMOUT):
            self.arr[i].set_color("green")
            self.canvas.update()
            # time.sleep(0.001)

    def bubble_sort(self):
        for i in range(SORTING_ELEMENT_AMOUT):
            for j in range(0, SORTING_ELEMENT_AMOUT-i-1):
                if self.arr[j+1].get_value() > self.arr[j].get_value():
                    Element.swapElementValue(self.arr[j+1], self.arr[j])
                self.arr[j+1].set_color("white")
                self.arr[j].set_color("red")
                self.canvas.update()
        
        self.__paint_sorted("green")
      
        
        