"""
filename: db.py
author: alexbozhinov
created: 05.02.2023
purpose: main file of the database module, where all database's tables are created
"""

from database.employees.chefs_db import ChefDB


class DB:
    def __init__(self):
        pass

    """
    method purpose: create tables for each model
    """
    @staticmethod
    def create_database():
        ChefDB.create_table()
