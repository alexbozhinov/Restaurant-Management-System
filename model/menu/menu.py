"""
filename: menu.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Menu
"""


class Menu:
    def __init__(self, food_items: list, drink_items: list):
        self.__food_items = food_items
        self.__drink_items = drink_items

    """
    Accessor methods:
    """
    def get_food_items(self):
        return self.__food_items

    def get_drink_items(self):
        return self.__drink_items

    """
    Mutator methods:
    """
    def set_food_items(self, new_food_items):
        self.__food_items = new_food_items

    def set_drink_items(self, new_drink_items):
        self.__drink_items = new_drink_items

    def select_item(self):
        pass

    def order_item(self):
        pass

    def update_menu(self):
        pass

