"""
filename: storage.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Storage
"""
import constants


class Storage:
    def __init__(self, ingredients: list):
        self.__ingredients = ingredients
        self.__storage_sizes = constants.STORAGE_SIZES
        self.__queries = []
        self.__deliveries = []

    def get_ingredients(self):
        return self.__ingredients

    def get_storage_sizes(self):
        return self.__storage_sizes

    def get_queries(self):
        return self.__queries

    def get_deliveries(self):
        return self.__deliveries
