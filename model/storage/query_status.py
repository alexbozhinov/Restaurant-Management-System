"""
filename: query_status.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class QueryStatus enumeration
"""

import enum


class QueryStatus(enum.Enum):
    CREATED = 1
    EDITED = 2
    CANCELED = 3
    ACCEPTED = 4
    UNDEFINED = 5
