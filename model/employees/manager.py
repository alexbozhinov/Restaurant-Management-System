"""
filename: chef.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class Manager, which inherits Employee, StorageManager and EmployeesManager
"""
from model.employees.chef import Chef
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

    def accept_ingredient_query(self):
        pass


"""
# manual test
m = Manager("Aleks Veselinov Bozhinov", "00000000000")
c = Chef('Ivan Angelov Angelov', '5555555555')
c.set_salary('1000.0')
print(c.get_salary().get_money())
m.update_employee_salary(c, 10)
print(c.get_salary().get_money())
"""