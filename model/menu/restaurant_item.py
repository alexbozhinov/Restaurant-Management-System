"""
filename: restaurant_item.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class RestaurantItem
"""
import constants
from model.employees.money import Money
from model.storage.measure import Measure


class RestaurantItem:
    def __init__(self, name=constants.UNDEFINED_CLASS_FIELD, quantity=0.0, measure=Measure.UNDEFINED,
                 price=Money(constants.UNDEFINED_MONEY_VALUE)):
        self._name = name
        self._quantity = quantity
        self._measure = measure
        self._price = price
        # validate all set methods through project

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_measure(self):
        return self._measure

    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name

    def set_quantity(self, new_quantity):
        self._quantity = new_quantity

    def set_measure(self, new_measure):
        self._measure = new_measure

    def set_price(self, new_price):
        self._price = new_price
