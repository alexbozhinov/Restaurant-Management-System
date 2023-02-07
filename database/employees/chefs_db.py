"""
filename: chefs_db.py
author: alexbozhinov
created: 06.02.2023
purpose: creating and managing of database's table chefs
"""

import sqlite3

from database.employees.employees_db import EmployeesDB


class ChefDB(EmployeesDB):
    """
    method purpose: creation of database's table chefs with all properties of model Chef
    """
    @staticmethod
    def create_table():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists chefs(
                name TEXT,
                identification_number TEXT PRIMARY KEY,
                email TEXT,
                username TEXT,
                password TEXT,
                salary DECIMAL,
                chef_type INTEGER,
                meals_cocked INTEGER,
                ingredient_orders_created INTEGER,
                current_orders INTEGER)
            """)

        conn.commit()
        conn.close()
        # self.__initial_submit()

    """
    method purpose: get a list of all chefs from the database's table chefs
    """
    @staticmethod
    def get_all():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM chefs")
        chefs = c.fetchall()

        conn.commit()
        conn.close()

        return chefs

    """
    method purpose: used one time for initial filling of database's table chefs
    """

    """
    @staticmethod
    def __initial_submit():
        all_chefs = [
            ('Ivan Kamenov Ivanov', '8602131486', 'ivan_ivanov@emp.com', 'iivanov', '12345', '1062', 3, 0, 0, 0),
            ('Krasen Stefanov Ivanov', '8206181426', 'krasen_ivanov@emp.com', 'kivanov', '55555', '1230', 2, 0, 0, 0),
        ('Kalina Plamenova Petkova', '9203201455', 'kalina_petkova@emp.com', 'kpetkova', '99999', '980', 5, 0, 0, 0),
        ]
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.executemany("INSERT INTO chefs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", all_chefs)

        conn.commit()
        conn.close()
    """