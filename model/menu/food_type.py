"""
filename: food_type.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class FoodType enumeration
"""
import enum


class FoodType(enum.Enum):
    SALAD = 0
    SOUP = 1
    CHICKEN = 2
    BEEF = 3
    PORK = 4
    FISH = 5
    DUCK = 6
    TURKEY = 7
    DESSERT = 8
    PASTA = 9
    PIZZA = 10
    BURGER = 11
    VEGETARIAN = 12
    UNDEFINED = 13
