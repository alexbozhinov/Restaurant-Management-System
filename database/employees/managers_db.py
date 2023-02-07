"""
filename: managers_db.py
author: alexbozhinov
created: 07.02.2023
purpose: creating and managing of database's table managers
"""

import sqlite3

from database.employees.employees_db import EmployeesDB


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
                salary DECIMAL)
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
        all_managers = [
            ('Aleks Veselinov Bozhinov', '0043201515', 'aleks_bozhinov@emp.com', 'abozhinov', '00000', '2500')
        ]
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.executemany("INSERT INTO managers VALUES (?, ?, ?, ?, ?, ?)", all_managers)

        conn.commit()
        conn.close()
    """
