import random
import time
from tkinter import Canvas

from config import *


class Element:

    def __init__(self, canvas: Canvas, posX1: int, posY1: int, posX2: int, value: int, color="white"):
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

    def set_value(self, value: int):
        self.value = value

    def set_color(self, color: str):
        self.color = color
        self.canvas.itemconfig(self.id, fill=color)


class ElementsManager:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.ELEMENT_AMOUT = 50
        self.ELEMENT_WIDTH = WINDOW_WIDTH/self.ELEMENT_AMOUT * 0.9
        self.SORTING_DELAY = 0
        self.isSorting = False
        self.createElements()

    def change_sorting_state(self):
        if self.isSorting == False:
            self.isSorting = True
        else:
            self.isSorting = False

    def set_element_quantity(self, quantity: int):
        if quantity < 1:
            raise ValueError("Wrong argument set_element_quantity()")
        self.ELEMENT_AMOUT = quantity
        self.ELEMENT_WIDTH = WINDOW_WIDTH/self.ELEMENT_AMOUT * 0.9

    def set_sotring_delay(self, delay: float):
        if delay < 0:
            ValueError("Wrong argument set_sorting_delay()")
        self.SORTING_DELAY = delay

    def createElements(self):
        self.canvas.delete("all")
        self.arr = []
        posX1 = 0
        posY1 = WINDOW_HEIGHT * 0.65

        for i in range(self.ELEMENT_AMOUT):
            posX2 = posX1 + self.ELEMENT_WIDTH
            posY2 = posY1 - random.randint(1, WINDOW_HEIGHT * 0.65)
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
                if not self.isSorting:
                    break
                if self.arr[j+1].get_value() > self.arr[j].get_value():
                    Element.swapElementValue(self.arr[j+1], self.arr[j])
                self.canvas.update()
                if self.SORTING_DELAY > 0:
                    time.sleep(self.SORTING_DELAY)

        self.__paint_sorted("green")

    def insertion_sort(self):
        for i in range(1, self.ELEMENT_AMOUT):
            j = i
            while j > 0 and self.arr[j-1].get_value() < self.arr[j].get_value():
                if not self.isSorting:
                    break
                Element.swapElementValue(self.arr[j], self.arr[j-1])
                self.canvas.update()
                if self.SORTING_DELAY > 0:
                    time.sleep(self.SORTING_DELAY)
                j -= 1

        self.__paint_sorted("green")

    def selection_sort(self):
        for i in range(self.ELEMENT_AMOUT - 1):
            if not self.isSorting:
                break
            minpos = i
            for j in range(i+1, self.ELEMENT_AMOUT):
                if not self.isSorting:
                    break
                if self.arr[j].get_value() > self.arr[minpos].get_value():
                    minpos = j
                if self.SORTING_DELAY > 0:
                    time.sleep(self.SORTING_DELAY)
                self.canvas.update()
            Element.swapElementValue(self.arr[i], self.arr[minpos])

        self.__paint_sorted("green")

    def quick_sort(self):

        def sort(low=0, high=self.ELEMENT_AMOUT - 1):
            if low < high:
                if self.isSorting:
                    pi = func(low, high)
                    sort(low, pi - 1)
                    sort(pi + 1, high)

        def func(low, high):
            pivot = self.arr[high].get_value()
            i = low - 1
            for j in range(low, high):
                if not self.isSorting:
                    break
                if self.arr[j].get_value() > pivot:
                    i += 1
                    Element.swapElementValue(self.arr[j], self.arr[i])
                if self.SORTING_DELAY > 0:
                    time.sleep(self.SORTING_DELAY)
                self.canvas.update()

            Element.swapElementValue(self.arr[i+1], self.arr[high])
            self.canvas.update()
            return i + 1

        sort()
        self.__paint_sorted("green")

    def heap_sort(self):

        def heapify(n, i):
            if self.isSorting:
                largest = i
                l = 2 * i + 1
                r = 2 * i + 2

                if l < n and self.arr[i].get_value() > self.arr[l].get_value():
                    largest = l

                if r < n and self.arr[largest].get_value() > self.arr[r].get_value():
                    largest = r

                if largest != i:
                    Element.swapElementValue(self.arr[i], self.arr[largest])
                    if self.SORTING_DELAY > 0:
                        time.sleep(self.SORTING_DELAY)
                    self.canvas.update()
                    heapify(n, largest)

        def sort():
            n = len(self.arr)
            for i in range(n//2, -1, -1):
                if not self.isSorting:
                    break
                heapify(n, i)

            for i in range(n-1, 0, -1):
                if not self.isSorting:
                    break
                Element.swapElementValue(self.arr[i], self.arr[0])
                if self.SORTING_DELAY > 0:
                    time.sleep(self.SORTING_DELAY)
                self.canvas.update()
                heapify(i, 0)

        sort()
        self.__paint_sorted("green")
