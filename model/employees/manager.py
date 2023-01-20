"""
filename: chef.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Manager, which inherits Employee, StorageManager and EmployeesManager
"""
from model.employees.employee import Employee
from model.management.budget_manager import BudgetManager
from model.management.employees_manager import EmployeesManager
from model.management.kitchen_manager import KitchenManager
from model.management.order_manager import OrderManager
from model.management.salon_manager import SalonManager
from model.management.storage_manager import StorageManager
from model.management.menu_manager import MenuManager


class Manager(Employee, StorageManager, EmployeesManager, MenuManager, BudgetManager,
              SalonManager, KitchenManager, OrderManager):
    def __init__(self, name, identification_number):
        super().__init__(name, identification_number)

    def accept_ingredient_order(self):
        pass
