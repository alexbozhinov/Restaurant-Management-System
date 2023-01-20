"""
filename: measure.py
author: alexbozhinov
created: 19.01.2023
purpose: definition of measure type enumeration
"""

import enum


class Measure(enum.Enum):
    kg = 0
    liter = 1
    box = 2
    jar = 3
    slice = 4
    bucket = 5
    package = 6
    piece = 7
    UNDEFINED = 8