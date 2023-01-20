"""
filename: query.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Query
"""
from model.employees.money import Money
from model.storage.query_status import QueryStatus


class Query:
    def __init__(self, created_by, ingredients=[]):
        self.__id = id(self)
        self.__created_by = created_by
        self.__ingredients = ingredients
        self.__total_price = Money()
        self.__status = QueryStatus.UNDEFINED

    def add_ingredient(self):
        pass

    def remove_ingredient(self):
        pass

    def edit_ingredient(self):
        pass # change quantity

    def calculate_total_price(self):
        pass

    def update_status(self, new_status: QueryStatus):
        self.__status = new_status
