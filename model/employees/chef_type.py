"""
filename: chef.py
author: alexbozhinov
created: 19.01.2023
purpose: definition of chef type enumeration
"""
import enum


class ChefType(enum.Enum):
    CHEF_OWNER = 0
    EXECUTIVE_CHEF = 1
    SOUS_CHEF = 2
    SENIOR_CHEF = 3
    PASTRY_CHEF = 4
    SAUCE_CHEF = 5
    FISH_CHEF = 6
    CONFECTIONER_CHEF = 7
    VEGETABLE_CHEF = 8
    MEAT_CHEF = 9
    PANTRY_CHEF = 10
    FRY_CHEF = 11
    GRILL_CHEF = 12
    BUTCHER_CHEF = 13

