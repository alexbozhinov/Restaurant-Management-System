"""
filename: managers_controller.py
author: alexbozhinov
created: 07.02.2023
purpose: main business logic for model Manager and controller implementation of MVC architecture
"""
from database.employees.managers_db import ManagerDB
from model.employees.manager import Manager


class ManagersController:
    def __init__(self):
        self.__managers = []  # stores all managers from the database
        self.__set_managers()

    """
    method purpose: check if imputed email and password in the login screen exist in the database
    """
    def check_login(self, email, password):
        for manager in self.__managers:
            if manager.get_email() == email and manager.is_valid_password(password):
                return True
        return False

    """
    method purpose: set list of all managers from the database
    """
    def __set_managers(self):
        managers = ManagerDB.read_all()

        for manager in managers:
            new_manager = Manager(manager[0], manager[1])  # 0: name, 1: identification_number
            new_manager.set_email(manager[2])
            new_manager.set_username(manager[3])
            new_manager.set_password(manager[4])
            new_manager.set_salary(manager[5])
            self.__managers.append(new_manager)

    def get_managers(self):
        return self.__managers
