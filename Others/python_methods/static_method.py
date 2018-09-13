#!/usr/bin/python3

# Link - https://www.youtube.com/watch?v=PNpt7cFjGsM

import math

# Creating different pizzas with its ingredients
class Pizza:
    # radius unit not defined in this
    def __init__(self, pizza_name, radius, ingredients):
        self.pizza_name = pizza_name
        self.radius = radius
        self.integredients = ingredients

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

    # Defining a Factory method using classmethod to create various pizza's
    @classmethod
    def margarita(cls, radius):
        return cls('margarita', radius, ['cheese', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls, radius):
        return cls('prosciutto', radius, ['cheese', 'tomatoes', 'ham'])

    @classmethod
    def piza3(cls, radius):
        return cls('piza3', radius, ['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def getIngredients(self):
        return self.integredients
    
    def area(self):
        return type(self)._circle_area(self.radius)

margarito = Pizza.margarita(5)
print(margarito)
prosciutto = Pizza.prosciutto(6)
print(prosciutto)
piza3 = Pizza.piza3(7)
print(piza3)

print()

print(Pizza._circle_area)
print(Pizza._circle_area(5))
print(Pizza._circle_area(6))
print(Pizza._circle_area(7))

print()

print(margarito.area())
print(prosciutto.area())
print(piza3.area())

print()

'''
Output:

<__main__.Pizza object at 0x000002B327E653C8>
<__main__.Pizza object at 0x000002B327E65C18>
<__main__.Pizza object at 0x000002B327E8B518>

<function Pizza._circle_area at 0x000002B327EA6378>
78.53981633974483
113.09733552923255
153.93804002589985

78.53981633974483
113.09733552923255
153.93804002589985
'''