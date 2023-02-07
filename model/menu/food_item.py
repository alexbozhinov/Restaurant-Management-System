"""
filename: food_item.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class FoodItem
"""
import constants
from model.employees.money import Money
from model.menu.food_type import FoodType
from model.menu.restaurant_item import RestaurantItem
from model.storage.measure import Measure


class FoodItem(RestaurantItem):
    def __init__(self, name=constants.UNDEFINED_CLASS_FIELD,
                 quantity=0.0,
                 measure=Measure.UNDEFINED,
                 price=Money(constants.UNDEFINED_MONEY_VALUE),
                 food_type=FoodType.UNDEFINED,
                 cocking_time=constants.UNDEFINED_CLASS_FIELD):
        super().__init__(name, quantity, measure, price)
        self.__food_type = food_type
        self.__cocking_time = cocking_time
        self.__recipe = constants.UNDEFINED_CLASS_FIELD
        self.__ingredients = []

    """
    Accessor methods:
    """
    def get_type(self):
        return self.__food_type

    def get_cocking_time(self):
        return self.__cocking_time

    def get_recipe(self):
        return self.__recipe

    def get_ingredients(self):
        return self.__ingredients

    """
    Mutator methods:
    """
    def set_type(self, new_type):
        self.__food_type = new_type

    def set_cocking_time(self, new_cocking_time):
        self.__cocking_time = new_cocking_time

    def set_recipe(self, recipe: str):
        self.__recipe = recipe

    def set_ingredients(self, ingredients: list):
        self.__ingredients = ingredients

    def cock_item(self):
        pass  # get items from storage
