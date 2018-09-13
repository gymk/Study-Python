#!/usr/bin/python3

# Link - https://www.youtube.com/watch?v=PNpt7cFjGsM

# Creating different pizzas with its ingredients
class Pizza:
    def __init__(self, ingredients):
        self.integredients = ingredients

    # Defining a Factory method using classmethod to create various pizza's
    @classmethod
    def margarita(cls):
        return cls(['cheese', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham'])

    @classmethod
    def piza3(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def getIngredients(self):
        return self.integredients

print(Pizza.margarita())
print(Pizza.prosciutto)
print(Pizza.prosciutto)

'''
Output:

<__main__.Pizza object at 0x000002B327E65D30>
<bound method Pizza.prosciutto of <class '__main__.Pizza'>>
<bound method Pizza.prosciutto of <class '__main__.Pizza'>>
'''