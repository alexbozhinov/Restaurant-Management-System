"""
filename: employees_db.py
author: alexbozhinov
created: 06.02.2023
purpose: Interface EmployeesDB to be inherited from all ChefsDB, WaitersDB and ManagerDB
"""


class EmployeesDB:
    def __init__(self):
        pass

    @staticmethod
    def create_table():
        pass

    @staticmethod
    def add():
        pass

    @staticmethod
    def get():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def get_all():
        pass
