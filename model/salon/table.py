"""
filename: table.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Table
"""


class Table:
    def __init__(self, table_form, seats, orders: list):
        self.__table_form = table_form
        self.__seats = seats
        self.__orders = orders

    """
    Accessor methods:
    """
    def get_table_form(self):
        return self.__table_form

    def get_seats(self):
        return self.__seats

    def get_orders(self):
        return self.__orders

    """
    Mutator methods:
    """
    def set_table_form(self, new_form):
        self.__table_form = new_form

    def set_seats(self, new_seats):
        self.__seats = new_seats

    """
    method purpose: add order for the table
    """
    def add_order(self, order):
        self.__orders.append(order)

    """
    method purpose: edit table's order
    """
    def edit_order(self, order):
        if order in self.__orders:
            pass

    """
    method purpose: remove order from the table list of orders
    """
    def remove_order(self, order):
        if order in self.__orders:
            self.__orders.remove(order)

    """
    method purpose: return property the current opened order of the table
    """
    @property
    def opened_order(self):
        if len(self.__orders > 0):
            return self.__orders[-1]

