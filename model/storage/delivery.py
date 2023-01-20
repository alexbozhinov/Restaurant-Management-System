"""
filename: delivery.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Delivery
"""
from model.storage.delivery_status import DeliveryStatus
from model.storage.query import Query


class Delivery:
    def __init__(self, query: Query):
        self.__query = query
        self.__status = DeliveryStatus.UNDEFINED
        self.__delivery_time = None  # date and clock

    def get_query(self):
        return self.__query

    def get_status(self):
        return self.__status

    def get_delivery_time(self):
        return self.__delivery_time

    def update_status(self, new_status: DeliveryStatus):
        self.__status = new_status
