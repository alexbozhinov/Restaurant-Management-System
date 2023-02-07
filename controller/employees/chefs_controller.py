"""
filename: chefs_controller.py
author: alexbozhinov
created: 06.02.2023
purpose: main business logic for model Chef and controller implementation of MVC architecture
"""

from database.employees.chefs_db import ChefDB
from model.employees.chef import Chef


class ChefsController:
    def __init__(self):
        self.__chefs = []  # stores all chefs from the database
        self.__set_chefs()

    """
    method purpose: check if imputed email and password in the login screen exist in the database
    """
    def check_login(self, email, password):
        for chef in self.__chefs:
            if chef.get_email() == email and chef.get_password() == password:
                return True
        return False

    """
    method purpose: set list of all chefs from the database
    """
    def __set_chefs(self):
        chefs = ChefDB.read_all()

        for chef in chefs:
            new_chef = Chef(chef[0], chef[1], chef[6])  # 0: name, 1: identification_number, 6: chef_type
            new_chef.set_email(chef[2])
            new_chef.set_username(chef[3])
            new_chef.set_password(chef[4])
            new_chef.set_salary(chef[5])
            new_chef.set_meals_cocked(chef[7])
            new_chef.set_ingredient_orders_created(chef[8])
            new_chef.set_current_orders(chef[9])
            self.__chefs.append(new_chef)

    def get_employees(self):
        return self.__chefs
