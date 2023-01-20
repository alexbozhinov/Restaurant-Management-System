"""
filename: salary_manager.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class SalaryManager
"""
from model.employees.employee import Employee
from decimal import Decimal


class SalaryManager:
    @staticmethod
    def update_employee_salary(employee: Employee, percentage=Decimal(0.0)):
        employee.update_salary(percentage)
