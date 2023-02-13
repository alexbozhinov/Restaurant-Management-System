"""
filename: waiters_db.py
author: alexbozhinov
created: 07.02.2023
purpose: creating and managing of database's table waiters
"""

import sqlite3

from database.employees.employees_db import EmployeesDB


class WaiterDB(EmployeesDB):
    """
    method purpose: creation of database's table waiters with all properties of model Waiter
    """
    @staticmethod
    def create_table():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists waiters(
                name TEXT,
                identification_number TEXT PRIMARY KEY,
                email TEXT,
                username TEXT,
                password TEXT,
                salary DECIMAL,
                number_of_tables INTEGER,
                number_of_orders INTEGER)
            """)

        conn.commit()
        conn.close()

    """
    method purpose: get a list of all waiters from the database's table waiters
    """
    @staticmethod
    def read_all():
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM waiters")
        waiters = c.fetchall()

        conn.commit()
        conn.close()

        return waiters

    # to test:
    @staticmethod
    def put(waiter):
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("INSERT INTO waiters VALUES("
                  "waiter.get_name(),"
                  "waiter.get_identification_number(),"
                  "waiter.get_email(),"
                  "waiter.get_username(),"
                  "waiter.get_password(),"
                  "waiter.get_salary(),"
                  "waiter.get_number_of_tables(),"
                  "waiter.get_number_of_orders()"
                  ")")

        conn.commit()
        conn.close()

    @staticmethod
    def read(identification_number):
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.execute("SELECT * FROM waiters WHERE identification_number = {identification_number}")  # to check
        waiter = c.fetchone()

        conn.commit()
        conn.close()

        return waiter

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    """
    method purpose: used one time for initial filling of database's table waiters
    """
    """
    @staticmethod
    def initial_insert():
        all_waiters = [
            ('Gergana Ivanova Petrova', '8504211485', 'gergana_petrova@emp.com', 'gpetrova', '11111', '900', 5, 0),
            ('Vasil Yordanov Draganov', '8108101414', 'vasil_draganov@emp.com', 'vdraganov', '33333', '1020', 7, 0),
            ('Vesela Plamenova Yordanova', '9405211451', 'vesela_yordanova@emp.com', 'vyordanova', '66666', '920', 5, 0)
        ]
        conn = sqlite3.connect('RMS.sqlite')
        c = conn.cursor()

        c.executemany("INSERT INTO waiters VALUES (?, ?, ?, ?, ?, ?, ?, ?)", all_waiters)

        conn.commit()
        conn.close()
    """
