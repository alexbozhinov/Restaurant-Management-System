"""
filename: delivery_status.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class DeliveryStatus
"""
import enum


class DeliveryStatus(enum.Enum):
    OPENED = 0
    CONFIRMED = 1
    TRAVELLING = 2
    DELIVERED = 3
    CLOSED = 4
    UNDEFINED = 5
