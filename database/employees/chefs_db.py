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

    """
    method purpose: get a list of all chefs from the database's table chefs
    """
    @staticmethod
    def read_all():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM chefs")
        chefs = c.fetchall()

        conn.commit()
        conn.close()

        return chefs

    # to test:
    @staticmethod
    def put(chef):
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO chefs VALUES("
                  "chef.get_name(),"
                  "chef.get_identification_number(),"
                  "chef.get_email(),"
                  "chef.get_username(),"
                  "chef.get_password(),"
                  "chef.get_salary(),"
                  "chef.get_chef_type(),"
                  "chef.get_meals_cocked(),"
                  "chef.get_ingredient_orders_created,"
                  "chef.get_current_orders() "
                  ")")

        conn.commit()
        conn.close()

    @staticmethod
    def read(identification_number):
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM chefs WHERE identification_number = {identification_number}")  # to check
        chef = c.fetchone()

        conn.commit()
        conn.close()

        return chef

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    """
    method purpose: used one time for initial filling of database's table chefs
    """
    """
    @staticmethod
    def initial_insert():
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
