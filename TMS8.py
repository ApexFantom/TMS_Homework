import time
import math
import matplotlib.pyplot as plt
import numpy as np
# Задание 1: Создание родительского класса auto, добавить атрибуты и методы согласно 1 заданию

class Auto():
    brand = "non"
    age = 0
    color = "non"
    mark = "non"
    weight = 1.3

    def __init__(self, brand = "Lexus", age = "15", mark = "subMark"):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
         print("move")

    def stop(self):
         print("stop")

    def birthday(self):
        self.age += 1


# Задание 2: создать два класса, наследующие класс auto, добавить новые атрибуты и методы, наследующие методы улучшить через супер

class Truck(Auto):
    max_load = 5
    def move(self):
        super().move()
        print("attention!")
    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    max_speed = 200
    def move(self):
        super().move()
        print("max speed is ", self.max_speed)

lamba = Car()
lamba.max_speed = 400
lamba.move()
rocketCar = Car()
rocketCar.move()
maz = Truck()
maz.max_load = 10
maz.move()
megaMaz = Truck()
megaMaz.max_load = 100
megaMaz.load()

#  задание 3*: для класса Circle реализовать метод, производящий вычитание двух окружностей, вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковам значением радиуса, то результатом вычитания будет точка Point

class Point():
    radius = 0
    colour = 'black'

class Circle(Point):
    patchList = []
    def __init__(self, radius = 0, colour = 'black'):
        self.colour = colour
        self.radius = radius
    @staticmethod
    def dif(a,b):
        patchList = []
        if abs(a.radius - b.radius) == 0:
            p = Point()
            patchList.append(plt.Circle((0, 0), 0, color='black', fill=True))
            Circle.vis()
            return p
        else:
            if (a.radius > b.radius):
                Circle.patchList.append(plt.Circle((0, 0), a.radius, color=a.colour, fill=True))
                Circle.patchList.append(plt.Circle((0, 0), b.radius, color=b.colour, fill=True))
            else:
                Circle.patchList.append(plt.Circle((0, 0), b.radius, color=b.colour, fill=True))
                Circle.patchList.append(plt.Circle((0, 0), a.radius, color=a.colour, fill=True))
            Circle.patchList.append(plt.Circle((0, 0), (a.radius - b.radius), color='white', fill=True))
            Circle.vis()
            return abs(a.radius - b.radius) * 2 * math.pi
    @staticmethod
    def vis():
        #сделал визуализацию через матплотлиб, темносерый - большой круг уменьшаемое, светлосерый - вычитаемое, и белый в середине - разность
        ax = plt.gca()
        for element in Circle.patchList:
            ax.add_patch(element)
        plt.axis('scaled')
        plt.show()


bigCircle = Circle(20, "grey")
smallCircle = Circle(11, "Lightgrey")
print(Circle.dif(bigCircle, smallCircle))


