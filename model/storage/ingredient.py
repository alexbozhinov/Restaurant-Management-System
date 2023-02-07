"""
filename: ingredient.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Ingredient
"""
from model.employees.money import Money
from model.storage.measure import Measure


class Ingredient:
    def __init__(self, name: str, measure: Measure, quantity: int, market_price: Money):
        self.__name = name
        self.__measure = measure
        self.__quantity = quantity
        self.__market_price = market_price

    """
    Accessor methods:
    """
    def get_name(self):
        return self.__name

    def get_measure(self):
        return self.__measure

    def get_quantity(self):
        return self.__quantity

    def get_market_price(self):
        return self.__market_price

    """
    Mutator methods:
    """
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def set_market_price(self, new_market_price: Money):
        self.__market_price = new_market_price
