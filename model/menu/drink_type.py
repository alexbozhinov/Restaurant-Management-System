"""
filename: drink_type.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class DrinkType enumeration
"""
import enum


class DrinkType(enum.Enum):
    ALCOHOL = 0
    JUICE = 1
    FIZZY_DRINK = 2
    SOFT_DRINK = 3
    HOT_DRINK = 4
    UNDEFINED = 5
