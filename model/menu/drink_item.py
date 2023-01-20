"""
filename: drink_item.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class DrinkItem
"""
import constants
from model.employees.money import Money
from model.menu.drink_type import DrinkType
from model.menu.restaurant_item import RestaurantItem
from model.storage.measure import Measure


class DrinkItem(RestaurantItem):
    def __init__(self, name=constants.UNDEFINED_CLASS_FIELD, quantity=0.0, measure=Measure.UNDEFINED,
                 price=Money(constants.UNDEFINED_MONEY_VALUE), drink_type=DrinkType.UNDEFINED):
        super().__init__(name, quantity, measure, price)
        self.__drink_type = drink_type

    def get_drink_type(self):
        return self.__drink_type

    def set_drink_type(self, new_drink_type):
        self.__drink_type = new_drink_type

    def bring_drink(self):
        pass  # get drink from storage
