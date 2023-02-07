"""
filename: waiters_controller.py
author: alexbozhinov
created: 07.02.2023
purpose: main business logic for model Waiter and controller implementation of MVC architecture
"""

from database.employees.waiters_db import WaiterDB
from model.employees.waiter import Waiter


class WaitersController:
    def __init__(self):
        self.__waiters = []  # stores all waiters from the database
        self.__set_waiters()

    """
    method purpose: check if imputed email and password in the login screen exist in the database
    """
    def check_login(self, email, password):
        for waiter in self.__waiters:
            if waiter.get_email() == email and waiter.get_password() == password:
                return True
        return False

    """
    method purpose: set list of all waiters from the database
    """
    def __set_waiters(self):
        waiters = WaiterDB.read_all()

        for waiter in waiters:
            new_waiter = Waiter(waiter[0], waiter[1])  # 0: name, 1: identification_number
            new_waiter.set_email(waiter[2])
            new_waiter.set_username(waiter[3])
            new_waiter.set_password(waiter[4])
            new_waiter.set_salary(waiter[5])
            new_waiter.set_number_of_tables(waiter[6])
            new_waiter.set_number_of_orders(waiter[7])
            self.__waiters.append(new_waiter)

    def get_waiters(self):
        return self.__waiters
