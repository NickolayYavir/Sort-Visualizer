import numpy as np
from tkinter import Canvas
import time


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
        self.ELEMENT_AMOUT = 50
        self.ELEMENT_WIDTH = WINDOW_WIDTH/self.ELEMENT_AMOUT * 0.9
        self.SORTING_DELAY = 0
        self.isSorting = False
        self.createElements()

    def change_sorting_state(self):
        if self.isSorting == False: self.isSorting = True
        else : self.isSorting = False

    def set_element_quantity(self, quantity:int):
        if quantity < 1 : raise ValueError("Wrong argument set_element_quantity()")
        self.ELEMENT_AMOUT = quantity
        self.ELEMENT_WIDTH = WINDOW_WIDTH/self.ELEMENT_AMOUT * 0.9

    def set_sotring_delay(self, delay:float):
        if delay < 0 : ValueError("Wrong argument set_sorting_delay()")
        self.SORTING_DELAY = delay

    def createElements(self):
        self.canvas.delete("all")
        self.arr = []
        posX1 = 0
        posY1 = WINDOW_HEIGHT * 0.65

        for i in range(self.ELEMENT_AMOUT):
            posX2 = posX1 + self.ELEMENT_WIDTH
            posY2 = posY1 - np.random.randint(1, WINDOW_HEIGHT * 0.65)
            self.arr.append(Element(self.canvas, posX1, posY1, posX2, posY2, 'white'))
            posX1 += self.ELEMENT_WIDTH

    def __paint_sorted(self, color):
        if self.isSorting:
            for i in range(self.ELEMENT_AMOUT):
                self.arr[i].set_color(color)
                self.canvas.update()
            self.change_sorting_state()


    def bubble_sort(self):
        for i in range(self.ELEMENT_AMOUT):
            for j in range(0, self.ELEMENT_AMOUT-i-1):
                if not self.isSorting: break
                self.arr[j+1].set_color('red')
                if self.arr[j+1].get_value() > self.arr[j].get_value():
                    Element.swapElementValue(self.arr[j+1], self.arr[j])
                self.canvas.update()
                if self.SORTING_DELAY > 0: time.sleep(self.SORTING_DELAY)
                self.arr[j+1].set_color('white')
                self.arr[j].set_color('white')
        
        self.__paint_sorted("green")
        
    def insertion_sort(self):
            for i in range(1, self.ELEMENT_AMOUT):
                j = i
                while j > 0 and self.arr[j-1].get_value() < self.arr[j].get_value():
                    if not self.isSorting : break
                    self.arr[j-1].set_color('red')
                    Element.swapElementValue(self.arr[j], self.arr[j-1])
                    self.canvas.update()
                    if self.SORTING_DELAY > 0: time.sleep(self.SORTING_DELAY)
                    self.arr[j].set_color('white')
                    self.arr[j-1].set_color('white')
                    j -= 1

            self.__paint_sorted("green")
        
        