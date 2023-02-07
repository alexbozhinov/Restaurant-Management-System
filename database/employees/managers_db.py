"""
filename: managers_db.py
author: alexbozhinov
created: 07.02.2023
purpose: creating and managing of database's table managers
"""

import sqlite3

from database.employees.employees_db import EmployeesDB
from model.employees.manager import Manager


class ManagerDB(EmployeesDB):
    """
    method purpose: creation of database's table managers with all properties of model Manager
    """
    @staticmethod
    def create_table():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists managers(
                name TEXT,
                identification_number TEXT PRIMARY KEY,
                email TEXT,
                username TEXT,
                password TEXT,
                salary TEXT)
            """)

        conn.commit()
        conn.close()

    """
    method purpose: get a list of all managers from the database's table managers
    """
    @staticmethod
    def read_all():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM managers")
        managers = c.fetchall()

        conn.commit()
        conn.close()

        return managers

    """
    method purpose: used one time for initial filling of database's table managers
    """
    """
    @staticmethod
    def initial_insert():

        manager = Manager('Aleks Veselinov Bozhinov', '0043201515')
        manager.set_password('00000')
        manager.hash_password()
        manager.set_salary('2500.00')

        all_managers = [
            (manager.get_name(), manager.get_identification_number(), manager.get_email(),
             manager.get_username(), manager.get_password(), str(manager.get_salary().get_value()))
        ]

        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.executemany("INSERT INTO managers VALUES (?, ?, ?, ?, ?, ?)", all_managers)

        conn.commit()
        conn.close()
    """
